Guide d'utilisation
===================

L'application OC Lettings est un site web Django permettant de consulter
des biens en location et des profils d'utilisateurs.

URLs disponibles
----------------

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - URL
     - Nom
     - Description
   * - ``/``
     - ``index``
     - Page d'accueil du site
   * - ``/lettings/``
     - ``lettings:index``
     - Liste de tous les biens en location
   * - ``/lettings/<id>/``
     - ``lettings:letting``
     - Détail d'un bien (titre + adresse complète)
   * - ``/profiles/``
     - ``profiles:index``
     - Liste de tous les profils utilisateurs
   * - ``/profiles/<username>/``
     - ``profiles:profile``
     - Détail d'un profil (ville favorite)
   * - ``/admin/``
     - —
     - Interface d'administration Django

Interface d'administration
---------------------------

L'interface d'administration est disponible sur ``/admin/``.
Elle permet de créer, modifier et supprimer des ``Address``, ``Letting`` et ``Profile``.

Créer un super-utilisateur :

.. code-block:: bash

   cd src
   python manage.py createsuperuser

Surveillance des erreurs (Sentry)
----------------------------------

L'application est intégrée avec **Sentry** pour la surveillance des erreurs en production.
La variable d'environnement ``SENTRY_DSN`` doit être renseignée pour activer l'envoi des événements.

En développement, laisser ``SENTRY_DSN`` vide désactive Sentry silencieusement.

Fichiers statiques
------------------

Les fichiers statiques sont gérés par **WhiteNoise**.
En production (dans le conteneur Docker), ``collectstatic`` est exécuté automatiquement
au build de l'image et les fichiers sont servis directement par WhiteNoise sans besoin d'un serveur web externe.
