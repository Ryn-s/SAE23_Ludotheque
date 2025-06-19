from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView, FormView
)
from django.contrib import messages
from django.db.models import Avg
import csv, io

from .models import Jeu
from .forms import JeuImportForm
from gestion_categories.models import Categorie
from gestion_auteurs.models     import Auteur
from gestion_commentaires.models import Commentaire

class JeuListView(ListView):
    model = Jeu
    template_name = 'gestion_jeux/jeu_list.html'

class JeuDetailView(DetailView):
    model = Jeu
    template_name = 'gestion_jeux/jeu_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jeu = self.object
        commentaires = Commentaire.objects.filter(jeu=jeu)

        # Moyennes par type
        context['moy_pro'] = commentaires.filter(
            joueur__type='professionnel'
        ).aggregate(Avg('note'))['note__avg'] or 0.0

        context['moy_part'] = commentaires.filter(
            joueur__type='particulier'
        ).aggregate(Avg('note'))['note__avg'] or 0.0

        # Meilleur / pire commentaire
        context['best']  = commentaires.order_by('-note').first()
        context['worst'] = commentaires.order_by('note').first()

        return context

class JeuCreateView(CreateView):
    model = Jeu
    fields = ['titre', 'annee_sortie', 'photo_boite', 'editeur', 'categorie', 'auteur']
    template_name = 'gestion_jeux/jeu_form.html'
    success_url = reverse_lazy('gestion_jeux:list')

class JeuUpdateView(UpdateView):
    model = Jeu
    fields = ['titre', 'annee_sortie', 'photo_boite', 'editeur', 'categorie', 'auteur']
    template_name = 'gestion_jeux/jeu_form.html'
    success_url = reverse_lazy('gestion_jeux:list')

class JeuDeleteView(DeleteView):
    model = Jeu
    template_name = 'gestion_jeux/jeu_confirm_delete.html'
    success_url = reverse_lazy('gestion_jeux:list')

class JeuImportView(FormView):
    template_name = 'gestion_jeux/jeu_import.html'
    form_class    = JeuImportForm
    success_url   = reverse_lazy('gestion_jeux:list')

    def form_valid(self, form):
        f      = form.cleaned_data['fichier']
        data   = f.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(data))
        count  = 0

        for row in reader:
            cat, _ = Categorie.objects.get_or_create(
                nom=row['categorie_nom']
            )
            aut, _ = Auteur.objects.get_or_create(
                prenom=row['auteur_prenom'],
                nom=row['auteur_nom'],
                defaults={'age': 0}
            )
            Jeu.objects.create(
                titre        = row['titre'],
                annee_sortie = int(row['annee_sortie']),
                editeur      = row['editeur'],
                categorie    = cat,
                auteur       = aut
            )
            count += 1

        messages.success(self.request, f"{count} jeux importés avec succès.")
        return super().form_valid(form)
