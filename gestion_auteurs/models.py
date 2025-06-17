from django.db import models

class Auteur(models.Model):
    nom    = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age    = models.PositiveIntegerField()
    photo  = models.ImageField(upload_to='auteurs/', blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
