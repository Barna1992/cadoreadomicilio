# 🚀 Quick Start - Cadore a Domicilio

Guida rapida per avviare il progetto dopo le migliorie implementate.

## ⚡ Setup Veloce (5 minuti)

### 1. Clona e prepara l'ambiente

```bash
cd cadoreadomicilio

# Crea virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure
venv\Scripts\activate  # Windows

# Installa dipendenze
pip install -r requirements.txt
```

### 2. Configura le variabili d'ambiente

```bash
# Copia il template
cp .env.example .env

# Genera SECRET_KEY (esegui in Python)
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Modifica .env con la tua SECRET_KEY
nano .env  # o usa il tuo editor preferito
```

**Contenuto minimo .env per sviluppo:**
```env
SECRET_KEY=la-tua-secret-key-generata
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_ENV=development
```

### 3. Database e migrazioni

```bash
# Crea/aggiorna database
python manage.py makemigrations
python manage.py migrate

# Crea superuser (opzionale)
python manage.py createsuperuser
```

### 4. Compila il frontend

```bash
cd frontend
npm install
npm run build
cd ..
```

### 5. Avvia il server

```bash
export DJANGO_ENV=development  # Linux/Mac
# oppure
set DJANGO_ENV=development  # Windows

python manage.py runserver
```

✅ **Apri il browser:** http://localhost:8000

---

## 🐳 Setup con Docker (Ancora più veloce!)

### Prerequisiti
- Docker e Docker Compose installati

### Comandi

```bash
# 1. Configura .env (vedi sopra)
cp .env.example .env
# Modifica .env

# 2. Build e avvio
docker-compose up -d

# 3. Migrazioni
docker-compose exec web python manage.py migrate

# 4. (Opzionale) Crea superuser
docker-compose exec web python manage.py createsuperuser
```

✅ **Apri il browser:** http://localhost:8000

**Comandi utili:**
```bash
# Vedi logs
docker-compose logs -f web

# Ferma tutto
docker-compose down

# Riavvia solo Django
docker-compose restart web

# Shell Django
docker-compose exec web python manage.py shell
```

---

## 📋 Checklist Pre-Deploy Produzione

Prima di mettere in produzione:

- [ ] Generata SECRET_KEY unica e forte
- [ ] DEBUG=False in .env produzione
- [ ] ALLOWED_HOSTS configurato con dominio reale
- [ ] Email SMTP configurato e testato
- [ ] Database PostgreSQL configurato (non SQLite)
- [ ] Backup database esistente
- [ ] SSL/HTTPS attivo
- [ ] File statici raccolti: `python manage.py collectstatic`
- [ ] Test deployment: `python manage.py check --deploy`

---

## 🔧 Comandi Utili

### Django Management

```bash
# Crea nuova app
python manage.py startapp nome_app

# Shell interattiva
python manage.py shell

# Test
python manage.py test

# Check sicurezza
python manage.py check --deploy
```

### Database

```bash
# Nuove migrazioni
python manage.py makemigrations

# Applica migrazioni
python manage.py migrate

# Rollback migrazione
python manage.py migrate app_name migration_name

# SQL di una migrazione
python manage.py sqlmigrate locali 0001
```

### Frontend

```bash
cd frontend

# Sviluppo (con watch)
npm run dev

# Produzione (minificato)
npm run build
```

### Docker

```bash
# Build immagine
docker-compose build

# Avvio servizi
docker-compose up -d

# Stop servizi
docker-compose down

# Vedi tutti i container
docker-compose ps

# Logs specifico servizio
docker-compose logs -f db

# Esegui comando in container
docker-compose exec web python manage.py shell
```

