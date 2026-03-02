# ---- Build stage ----
FROM python:3.12.10-slim AS builder

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---- Final stage ----
FROM python:3.12.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copier les packages installés depuis le build stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copier le code source
COPY . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput
    
EXPOSE 8000

# Au démarrage : migrate (assure que le schéma DB est à jour), puis gunicorn.
# collectstatic est déjà exécuté dans le RUN ci-dessus et baked dans l'image.
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]