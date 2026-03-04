Déploiement
===========

Vue d'ensemble
--------------

Le déploiement est entièrement automatisé via un pipeline CI/CD GitHub Actions.
Chaque push sur la branche ``main`` déclenche la séquence suivante :

1. **Tests & linting** — pytest + flake8
2. **Build Docker** — construction et push de l'image sur GitHub Container Registry (GHCR)
3. **Déploiement** — déclenchement du webhook Render

Pipeline CI/CD (.github/workflows/ci-cd.yml)
--------------------------------------------

Job 1 — Build, Lint & Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Déclenché sur toutes les branches.

- Installation des dépendances depuis ``src/requirements.txt``
- Linting avec ``flake8``
- Tests avec ``pytest`` (couverture ≥ 80 %)

Job 2 — Build & Push Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Déclenché uniquement sur ``main``, après la réussite du Job 1.

- Connexion à ``ghcr.io`` via ``GITHUB_TOKEN``
- Build de l'image avec ``context: ./src``
- Push avec les tags ``latest`` et le SHA court du commit

Job 3 — Deploy to Render
~~~~~~~~~~~~~~~~~~~~~~~~~

Déclenché après la réussite du Job 2.

- Appel du webhook Render (``RENDER_DEPLOY_HOOK_URL``) pour redéployer le service

Secrets GitHub requis
---------------------

Les secrets suivants doivent être configurés dans **Settings > Secrets and variables > Actions** du dépôt :

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Nom du secret
     - Description
   * - ``SECRET_KEY``
     - Clé secrète Django utilisée pendant les tests
   * - ``RENDER_DEPLOY_HOOK_URL``
     - URL du deploy hook fournie par Render

.. note::
   ``GITHUB_TOKEN`` est automatiquement fourni par GitHub Actions, aucune configuration nécessaire.

Docker
------

Le ``Dockerfile`` se trouve dans ``src/``. Il utilise un build multi-stage :

- **Stage builder** — installe les dépendances pip
- **Stage final** — copie les packages et le code, exécute ``collectstatic`` et ``migrate``, puis lance ``gunicorn``

Pour builder l'image manuellement :

.. code-block:: bash

   docker build -t oc-lettings-site ./src
   docker run -p 8000:8000 --env-file .env oc-lettings-site

Render
------

Le service Render est configuré pour utiliser l'image Docker publiée sur GHCR.
Chaque déploiement est déclenché automatiquement via le webhook après un push sur ``main``.
