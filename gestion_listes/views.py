from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import ListeJeux

class ListeJeuxListView(ListView):
    model = ListeJeux
    template_name = 'gestion_listes/listejeux_list.html'

class ListeJeuxDetailView(DetailView):
    model = ListeJeux
    template_name = 'gestion_listes/listejeux_detail.html'

class ListeJeuxCreateView(CreateView):
    model = ListeJeux
    fields = ['joueur','jeu']
    template_name = 'gestion_listes/listejeux_form.html'
    success_url = reverse_lazy('gestion_listes:list')

class ListeJeuxDeleteView(DeleteView):
    model = ListeJeux
    template_name = 'gestion_listes/listejeux_confirm_delete.html'
    success_url = reverse_lazy('gestion_listes:list')
