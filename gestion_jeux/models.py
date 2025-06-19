from django.db import models
from gestion_categories.models import Categorie
from gestion_auteurs.models    import Auteur

class Jeu(models.Model):
    titre         = models.CharField(max_length=255)
    annee_sortie  = models.PositiveIntegerField()
    photo_boite   = models.ImageField(upload_to='jeux/', blank=True)
    editeur       = models.CharField(max_length=100)
    categorie     = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    auteur        = models.ForeignKey(Auteur,    on_delete=models.PROTECT)

    def __str__(self):
        return self.titre
