from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Avg
from .models import Joueur
from gestion_listes.models import ListeJeux
from gestion_listes.models      import ListeJeux
from gestion_commentaires.models import Commentaire

class JoueurListView(ListView):
    model = Joueur
    template_name = 'gestion_joueurs/joueur_list.html'

class JoueurDetailView(DetailView):
    model = Joueur
    template_name = 'gestion_joueurs/joueur_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        joueur = self.object

        
        listes = ListeJeux.objects.filter(joueur=joueur).select_related('jeu')
        context['listes'] = listes

        
        comments = Commentaire.objects.filter(joueur=joueur).select_related('jeu')
        context['comments'] = comments
       

        moy_qs = (
            Commentaire.objects
            .values('jeu')
            .annotate(moy=Avg('note'))
        )
        
        context['moyennes'] = {item['jeu']: item['moy'] for item in moy_qs}

        return context

class JoueurCreateView(CreateView):
    model = Joueur
    fields = ['nom', 'prenom', 'email', 'mot_de_passe', 'type']
    template_name = 'gestion_joueurs/joueur_form.html'
    success_url = reverse_lazy('gestion_joueurs:list')

class JoueurUpdateView(UpdateView):
    model = Joueur
    fields = ['nom', 'prenom', 'email', 'type']
    template_name = 'gestion_joueurs/joueur_form.html'
    success_url = reverse_lazy('gestion_joueurs:list')

class JoueurDeleteView(DeleteView):
    model = Joueur
    template_name = 'gestion_joueurs/joueur_confirm_delete.html'
    success_url = reverse_lazy('gestion_joueurs:list')
