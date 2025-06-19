from django.urls import path
from . import views

app_name = 'gestion_commentaires'
urlpatterns = [
    path('',            views.CommentaireListView.as_view(),   name='list'),
    path('new/',        views.CommentaireCreateView.as_view(), name='create'),
    path('<int:pk>/',   views.CommentaireDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/',   views.CommentaireUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CommentaireDeleteView.as_view(), name='delete'),
]
