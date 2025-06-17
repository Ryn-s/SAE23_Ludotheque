from django.urls import path
from . import views

app_name = 'gestion_jeux'
urlpatterns = [
    path('',            views.JeuListView.as_view(),   name='list'),
    path('new/',        views.JeuCreateView.as_view(), name='create'),
    path('<int:pk>/',   views.JeuDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/',   views.JeuUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.JeuDeleteView.as_view(), name='delete'),
    path('import/',     views.JeuImportView.as_view(), name='import'),  # si tu as ajouté l'import CSV
]
