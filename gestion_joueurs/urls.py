from django.urls import path
from . import views

app_name = 'gestion_joueurs'

urlpatterns = [
    path('',            views.JoueurListView.as_view(),   name='list'),
    path('new/',        views.JoueurCreateView.as_view(), name='create'),
    path('<int:pk>/',   views.JoueurDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/',   views.JoueurUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.JoueurDeleteView.as_view(), name='delete'),
]
