from whitenoise.storage import CompressedStaticFilesStorage  # noqa: F401

# CompressedStaticFilesStorage compresse les fichiers statiques (gzip/brotli)
# sans créer de manifest ni hacher les noms de fichiers.
# Cela évite l'erreur MissingFileError de CompressedManifestStaticFilesStorage
# lorsque le CSS référence des assets absents du dépôt (device mockups, etc.).
