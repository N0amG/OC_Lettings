Structure de la base de données
================================

Le projet utilise **SQLite** en développement (``src/oc-lettings-site.sqlite3``)
et peut être configuré avec n'importe quelle base Django en production.

L'ORM Django est utilisé pour toutes les opérations sur la base de données.

Application ``lettings``
------------------------

Address
~~~~~~~

Représente une adresse physique associée à un bien en location.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Champ
     - Type
     - Description
   * - ``number``
     - PositiveIntegerField
     - Numéro de rue (max 9999)
   * - ``street``
     - CharField(64)
     - Nom de la rue
   * - ``city``
     - CharField(64)
     - Ville
   * - ``state``
     - CharField(2)
     - Code d'état / région (2 caractères)
   * - ``zip_code``
     - PositiveIntegerField
     - Code postal (max 99999)
   * - ``country_iso_code``
     - CharField(3)
     - Code ISO du pays (3 caractères)

Letting
~~~~~~~

Représente un bien en location avec un titre et une adresse.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Champ
     - Type
     - Description
   * - ``title``
     - CharField(256)
     - Titre du bien
   * - ``address``
     - OneToOneField(Address)
     - Adresse associée (suppression en cascade)

Application ``profiles``
------------------------

Profile
~~~~~~~

Étend le modèle ``User`` de Django avec une ville favorite.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Champ
     - Type
     - Description
   * - ``user``
     - OneToOneField(User)
     - Utilisateur Django associé (suppression en cascade)
   * - ``favorite_city``
     - CharField(64)
     - Ville favorite (optionnel)

Relations
---------

.. code-block:: text

   User (Django) ──< Profile
   Address ──< Letting
