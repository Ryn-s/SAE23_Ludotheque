from django.db import models
from django.contrib.auth.hashers import make_password

class Joueur(models.Model):
    TYPE_CHOICES = [
        ('professionnel','Professionnel'),
        ('particulier','Particulier'),
    ]

    nom          = models.CharField(max_length=100)
    prenom       = models.CharField(max_length=100)
    email        = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    type         = models.CharField(max_length=13, choices=TYPE_CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.mot_de_passe = make_password(self.mot_de_passe)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
