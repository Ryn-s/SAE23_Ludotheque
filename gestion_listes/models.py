from django.db import models
from django.utils import timezone
from gestion_jeux.models      import Jeu
from gestion_joueurs.models    import Joueur

class ListeJeux(models.Model):
    joueur     = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    jeu        = models.ForeignKey(Jeu,     on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('joueur', 'jeu')

    def __str__(self):
        return f"{self.joueur} → {self.jeu}"
