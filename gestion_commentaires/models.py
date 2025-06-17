from django.db import models
from django.utils import timezone
from gestion_jeux.models      import Jeu
from gestion_joueurs.models    import Joueur

class Commentaire(models.Model):
    jeu         = models.ForeignKey(Jeu,    on_delete=models.CASCADE)
    joueur      = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    note        = models.PositiveSmallIntegerField()
    commentaire = models.TextField(blank=True)
    date        = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Note {self.note} par {self.joueur}"
