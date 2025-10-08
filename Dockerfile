# Dockerfile per Cadore a Domicilio
FROM python:3.11-slim

# Imposta variabili d'ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Crea directory di lavoro
WORKDIR /app

# Installa dipendenze di sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e installa dipendenze Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia il progetto
COPY . .

# Crea directory per file statici e media
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Colleziona file statici
RUN python manage.py collectstatic --noinput || true

# Espone porta 8000
EXPOSE 8000

# Script di avvio
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "cadoreadomicilio.wsgi:application"]
