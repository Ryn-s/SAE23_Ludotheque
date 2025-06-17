from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Commentaire

class CommentaireListView(ListView):
    model = Commentaire
    template_name = 'gestion_commentaires/commentaire_list.html'

class CommentaireDetailView(DetailView):
    model = Commentaire
    template_name = 'gestion_commentaires/commentaire_detail.html'

class CommentaireCreateView(CreateView):
    model = Commentaire
    fields = ['jeu','joueur','note','commentaire']
    template_name = 'gestion_commentaires/commentaire_form.html'
    success_url = reverse_lazy('gestion_commentaires:list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['jeu'].empty_label    = None
        form.fields['joueur'].empty_label = None
        return form

class CommentaireUpdateView(UpdateView):
    model = Commentaire
    fields = ['note','commentaire']
    template_name = 'gestion_commentaires/commentaire_form.html'
    success_url = reverse_lazy('gestion_commentaires:list')

class CommentaireDeleteView(DeleteView):
    model = Commentaire
    template_name = 'gestion_commentaires/commentaire_confirm_delete.html'
    success_url = reverse_lazy('gestion_commentaires:list')
