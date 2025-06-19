"""
URL configuration for ludotheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),

    path('categories/',     include('gestion_categories.urls', namespace='gestion_categories')),
    path('auteurs/',        include('gestion_auteurs.urls',    namespace='gestion_auteurs')),
    path('jeux/',           include('gestion_jeux.urls',       namespace='gestion_jeux')),
    path('joueurs/',        include('gestion_joueurs.urls',    namespace='gestion_joueurs')),
    path('commentaires/',   include('gestion_commentaires.urls', namespace='gestion_commentaires')),
    path('listes/',         include('gestion_listes.urls',     namespace='gestion_listes')),
]
