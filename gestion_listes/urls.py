from django.urls import path
from . import views

app_name = 'gestion_listes'
urlpatterns = [
    path('',            views.ListeJeuxListView.as_view(),   name='list'),
    path('new/',        views.ListeJeuxCreateView.as_view(), name='create'),
    path('<int:pk>/',   views.ListeJeuxDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.ListeJeuxDeleteView.as_view(), name='delete'),
]
