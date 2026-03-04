import pytest


@pytest.fixture(autouse=True)
def use_simple_static_storage(settings):
    """
    Remplace CompressedManifestStaticFilesStorage par le storage par défaut
    pour éviter l'erreur "Missing staticfiles manifest" (collectstatic
    n'est exécuté qu'en production dans le conteneur Docker).
    """
    settings.STORAGES = {
        **settings.STORAGES,
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
