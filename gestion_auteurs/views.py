from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Auteur

class AuteurListView(ListView):
    model = Auteur
    template_name = 'gestion_auteurs/auteur_list.html'

class AuteurDetailView(DetailView):
    model = Auteur
    template_name = 'gestion_auteurs/auteur_detail.html'

class AuteurCreateView(CreateView):
    model = Auteur
    fields = ['nom', 'prenom', 'age', 'photo']
    template_name = 'gestion_auteurs/auteur_form.html'
    success_url = reverse_lazy('gestion_auteurs:list')

class AuteurUpdateView(UpdateView):
    model = Auteur
    fields = ['nom', 'prenom', 'age', 'photo']
    template_name = 'gestion_auteurs/auteur_form.html'
    success_url = reverse_lazy('gestion_auteurs:list')

class AuteurDeleteView(DeleteView):
    model = Auteur
    template_name = 'gestion_auteurs/auteur_confirm_delete.html'
    success_url = reverse_lazy('gestion_auteurs:list')
