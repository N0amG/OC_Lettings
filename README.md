# OC Lettings

Site web d'Orange County Lettings — application Django de gestion de biens en location et de profils utilisateurs.


## Documentation

📖 **[Documentation complète sur Read the Docs](https://doc-lettings-site.readthedocs.io/fr/latest/)**

La documentation couvre :
- Installation locale
- Architecture du projet
- Configuration (variables d'environnement)
- Déploiement (CI/CD, Docker, Render)
- Structure de la base de données
- Guide d'utilisation

## Démarrage rapide

### Prérequis

- Python 3.12+
- Git
- Docker (optionnel, pour le déploiement)

### Installation locale

```bash
# Cloner le dépôt
git clone https://github.com/N0amG/OC_Lettings.git
cd Python-OC-Lettings-FR

# Créer et activer l'environnement virtuel
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1
# Linux / macOS
source venv/bin/activate

# Installer les dépendances
pip install -r src/requirements.txt

# Configurer les variables d'environnement
# Créer un fichier src/.env (voir la documentation pour le contenu)

# Lancer le serveur
cd src
python manage.py migrate
python manage.py runserver
```

L'application est accessible sur http://127.0.0.1:8000.

### Lancer l'image Docker en local

```bash
# Récupérer la dernière image
docker pull ghcr.io/n0amg/oc-lettings-site

# Lancer le conteneur
docker run -d -p 8000:8000 ghcr.io/n0amg/oc-lettings-site
```

L'application est alors accessible sur http://127.0.0.1:8000.

### Lancer les tests

Depuis la racine du projet :

```bash
pytest
```

### Linting

```bash
flake8 src/
```

## CI/CD

Chaque push sur `main` déclenche automatiquement :

1. Tests & linting (toutes les branches)
2. Build et push de l'image Docker sur GitHub Container Registry
3. Déploiement sur Render
