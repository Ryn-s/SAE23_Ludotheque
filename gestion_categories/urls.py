from django.urls import path
from . import views

app_name = 'gestion_categories'
urlpatterns = [
    path('',          views.CategorieListView.as_view(),   name='list'),
    path('new/',      views.CategorieCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CategorieDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/',   views.CategorieUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CategorieDeleteView.as_view(), name='delete'),
]
