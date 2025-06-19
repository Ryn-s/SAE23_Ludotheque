from django import forms

class JeuImportForm(forms.Form):
    fichier = forms.FileField(
        label="Fichier CSV des jeux",
        help_text="Colonnes : titre,annee_sortie,editeur,categorie_nom,auteur_prenom,auteur_nom"
    )
