Installation locale
===================

Prérequis
---------

- Python 3.12+
- Git
- Un terminal (PowerShell, bash, etc.)

Cloner le dépôt
---------------

.. code-block:: bash

   git clone https://github.com/<votre-compte>/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Créer et activer l'environnement virtuel
-----------------------------------------

.. code-block:: bash

   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python -m venv venv
   source venv/bin/activate

Installer les dépendances
--------------------------

.. code-block:: bash

   pip install -r src/requirements.txt

Configurer les variables d'environnement
-----------------------------------------

Créez un fichier ``.env`` à la racine du projet avec le contenu suivant :

.. code-block:: ini

   SECRET_KEY=votre_clé_secrète_django
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=          # optionnel, laisser vide en local

Lancer le serveur de développement
------------------------------------

.. code-block:: bash

   cd src
   python manage.py migrate
   python manage.py runserver

L'application est accessible sur http://127.0.0.1:8000.

Lancer les tests
----------------

Depuis la racine du projet :

.. code-block:: bash

   pytest

Le rapport de couverture s'affiche dans le terminal. La couverture minimale requise est de **80 %**.
