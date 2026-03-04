Configuration
=============

Toute la configuration sensible est gérée via des variables d'environnement,
chargées depuis un fichier ``.env`` à la racine de ``src/`` grâce à ``python-dotenv``.

Variables d'environnement
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 15 40

   * - Variable
     - Obligatoire
     - Défaut
     - Description
   * - ``SECRET_KEY``
     - Oui (prod)
     - ``dummy-key-for-development``
     - Clé secrète Django. Doit être longue, aléatoire et unique en production.
   * - ``DEBUG``
     - Non
     - ``False``
     - Active le mode debug Django. Mettre ``True`` uniquement en développement local.
   * - ``ALLOWED_HOSTS``
     - Non
     - ``localhost``
     - Liste des domaines autorisés, séparés par des virgules. Ex : ``localhost,mon-domaine.com``
   * - ``SENTRY_DSN``
     - Non
     - *(vide)*
     - DSN Sentry pour la surveillance des erreurs. Laisser vide pour désactiver.
   * - ``RENDER_EXTERNAL_HOSTNAME``
     - Non
     - *(vide)*
     - Injecté automatiquement par Render. Ajouté à ``ALLOWED_HOSTS`` si présent.

Exemple de fichier .env (développement local)
----------------------------------------------

.. code-block:: ini

   SECRET_KEY=django-insecure-exemple-cle-locale-a-changer
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=

.. warning::
   Ne jamais commiter le fichier ``.env`` dans le dépôt Git.
   Il est déjà référencé dans ``.gitignore``.

Configuration en production (Render)
--------------------------------------

Sur Render, les variables sont définies dans **Dashboard > Service > Environment**.
Les variables ``SECRET_KEY`` et ``SENTRY_DSN`` doivent y être renseignées.
``RENDER_EXTERNAL_HOSTNAME`` est injecté automatiquement par Render.

Configuration Django notable
-----------------------------

Base de données
~~~~~~~~~~~~~~~

SQLite en développement (``src/oc-lettings-site.sqlite3``).
En production dans Docker, la même base SQLite est utilisée — elle est créée
et migrée automatiquement au build de l'image via ``python manage.py migrate``.

Fichiers statiques
~~~~~~~~~~~~~~~~~~

Gérés par **WhiteNoise** via ``CompressedManifestStaticFilesStorage``.
``python manage.py collectstatic`` est exécuté au build Docker et copie les fichiers
dans ``src/staticfiles/``.

Internationalisation
~~~~~~~~~~~~~~~~~~~~

- Langue : ``fr``
- Fuseau horaire : ``UTC``
