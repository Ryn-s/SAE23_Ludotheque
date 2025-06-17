from django.urls import path
from . import views

app_name = 'gestion_auteurs'
urlpatterns = [
    path('',            views.AuteurListView.as_view(),   name='list'),
    path('new/',        views.AuteurCreateView.as_view(), name='create'),
    path('<int:pk>/',   views.AuteurDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/',   views.AuteurUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AuteurDeleteView.as_view(), name='delete'),
]
