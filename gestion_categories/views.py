from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categorie

class CategorieListView(ListView):
    model = Categorie
    template_name = 'gestion_categories/categorie_list.html'

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = 'gestion_categories/categorie_detail.html'

class CategorieCreateView(CreateView):
    model = Categorie
    fields = ['nom', 'descriptif']
    template_name = 'gestion_categories/categorie_form.html'
    success_url = reverse_lazy('gestion_categories:list')

class CategorieUpdateView(UpdateView):
    model = Categorie
    fields = ['nom', 'descriptif']
    template_name = 'gestion_categories/categorie_form.html'
    success_url = reverse_lazy('gestion_categories:list')

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'gestion_categories/categorie_confirm_delete.html'
    success_url = reverse_lazy('gestion_categories:list')
