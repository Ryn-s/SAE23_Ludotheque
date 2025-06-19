<!-- README.md -->

# Ludothèque SAE23

Ce dépôt contient :

1. **Application Django**  
   - Dossier `ludotheque/` avec le projet Django  
   - Dossier `gestion_*` pour chaque app (jeux, catégories, joueurs…)  
   - `manage.py` pour lancer le serveur

2. **Démo CSV**  
   - `jeux_demo.csv` : un exemple de fichier CSV (à créer)  
   -

---

## Installation

1. Cloner le dépôt  
   ```bash
   git clone git@github.com:Ryn-s/SAE23_Ludotheque.git
   cd SAE23_Ludotheque-MAIN

```bash
# 1. Crée et active un environnement virtuel
python3 -m venv venv
source venv/bin/activate       # sous Linux/macOS
venv\Scripts\activate.bat      # sous Windows

# 2. Installe les dépendances
pip install -r requirements.txt

Configurer la base MySQL dans ludotheque/settings.py
(hôte, utilisateur, mot de passe, nom de la base)

Appliquer les migrations :

python manage.py migrate

Lancer le serveur : 

python manage.py runserver

