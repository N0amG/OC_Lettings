Architecture du projet
======================

Le projet est une application Django structurée en plusieurs apps indépendantes,
toutes situées dans le dossier ``src/``.

Arborescence
------------

.. code-block:: text

   Python-OC-Lettings-FR/
   ├── .github/
   │   └── workflows/
   │       └── ci-cd.yml          # Pipeline CI/CD GitHub Actions
   ├── doc/
   │   └── source/                # Sources de la documentation Sphinx
   ├── src/
   │   ├── lettings/              # App : biens en location
   │   ├── profiles/              # App : profils utilisateurs
   │   ├── oc_lettings_site/      # App principale (settings, URLs racine)
   │   ├── templates/             # Templates globaux (base.html, 404, 500)
   │   ├── static/                # Fichiers statiques source
   │   ├── staticfiles/           # Fichiers statiques collectés (collectstatic)
   │   ├── manage.py
   │   ├── requirements.txt
   │   ├── Dockerfile
   │   └── conftest.py            # Fixtures pytest globales
   ├── setup.cfg                  # Configuration pytest et coverage
   ├── .readthedocs.yaml          # Configuration Read the Docs
   └── .env                       # Variables d'environnement (non versionné)

Apps Django
-----------

oc_lettings_site
~~~~~~~~~~~~~~~~

App principale du projet. Contient :

- ``settings.py`` — configuration globale (base de données, middleware, Sentry, WhiteNoise)
- ``urls.py`` — routage racine, inclut les URLs des apps ``lettings`` et ``profiles``
- ``views.py`` — vue de la page d'accueil

lettings
~~~~~~~~

Gère les biens en location. Expose :

- Les modèles ``Address`` et ``Letting``
- Les vues ``index`` (liste) et ``letting`` (détail)
- Les URLs sous le préfixe ``/lettings/``

profiles
~~~~~~~~

Gère les profils utilisateurs. Expose :

- Le modèle ``Profile`` (extension du ``User`` Django)
- Les vues ``index`` (liste) et ``profile`` (détail)
- Les URLs sous le préfixe ``/profiles/``

Flux de requête
---------------

.. code-block:: text

   Navigateur
       │
       ▼
   Gunicorn (production) / runserver (dev)
       │
       ▼
   WhiteNoise (fichiers statiques)
       │
       ▼
   Django Middleware
       │
       ▼
   oc_lettings_site/urls.py
       ├── /           → oc_lettings_site.views.index
       ├── /lettings/  → lettings.urls
       ├── /profiles/  → profiles.urls
       └── /admin/     → Django Admin
