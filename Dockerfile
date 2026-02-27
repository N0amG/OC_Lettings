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

# Collecter les fichiers statiques (SECRET_KEY temporaire uniquement pour collectstatic)
RUN SECRET_KEY=dummy-key-for-collectstatic \
    DEBUG=False \
    ALLOWED_HOSTS=localhost \
    python manage.py collectstatic --noinput

EXPOSE 8000

# Au démarrage : collectstatic (sécurité si staticfiles/ absent de l'image),
# migrate (assure que le schéma DB est à jour), puis gunicorn.
CMD sh -c "python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --log-level info"
