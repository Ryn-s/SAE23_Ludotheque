from django.db import models

class Categorie(models.Model):
    nom        = models.CharField(max_length=100)
    descriptif = models.TextField(blank=True)

    def __str__(self):
        return self.nom
