# 🏠 Cadore a Domicilio ⛰️

Una piattaforma web per mettere in contatto i commercianti del Cadore con i loro clienti, facilitando il servizio di consegna a domicilio e ritiro merce.

> 🚀 **Quick Start**: Per iniziare subito, consulta la [Guida Rapida (QUICKSTART.md)](QUICKSTART.md)
>
> ✨ **Novità**: Il progetto è stato aggiornato con importanti migliorie di sicurezza, performance e deployment. Vedi [MIGLIORIE_IMPLEMENTATE.md](MIGLIORIE_IMPLEMENTATE.md)

## 📋 Descrizione

**Cadore a Domicilio** è una web application sviluppata per supportare le attività commerciali della zona del Cadore (provincia di Belluno, Veneto) durante il periodo di emergenza COVID-19. Il progetto permette ai commercianti di registrare i propri servizi di consegna a domicilio o ritiro merce, rendendo più facile per i cittadini trovare e contattare le attività locali che offrono questi servizi.

## ✨ Funzionalità

- **Catalogo dei commercianti**: Visualizzazione interattiva di tutti i locali che offrono servizi di consegna
- **Filtri avanzati**: Possibilità di filtrare per comune, categoria merceologica e tipo di servizio
- **Form di registrazione**: I commercianti possono autonomamente inserire la propria attività
- **Informazioni dettagliate**: Per ogni locale vengono mostrati:
  - Orari di apertura (mattina/pomeriggio)
  - Giorni di chiusura
  - Servizi pranzo/cena
  - Modalità di consegna
  - Contatti (telefono, email, Facebook, sito web)
  - Comuni in cui effettuano consegne
- **REST API**: Endpoint API per l'integrazione con altri servizi
- **Notifiche email**: Sistema automatico di notifica quando un nuovo locale viene registrato

## 🛠️ Tecnologie Utilizzate

### Backend
- **Django 4.2.0 LTS** - Framework web Python (aggiornato da 3.0.4)
- **Django REST Framework 3.14.0** - Per le API RESTful
- **SQLite / PostgreSQL** - Database (SQLite dev, PostgreSQL produzione)
- **django-materializecss-form** - Form styling
- **Gunicorn** - WSGI server per produzione
- **python-decouple** - Gestione configurazione

### Frontend
- **React 16.13.1** - Libreria JavaScript per l'UI
- **Webpack 4.42.1** - Module bundler
- **Babel 7.9.0** - JavaScript transpiler
- **Materialize CSS** - Framework CSS per il design

## 🚀 Installazione e Setup

### Prerequisiti
- Python 3.x
- Node.js e npm
- pip (Python package manager)

### Backend Setup

1. Clona il repository:
```bash
git clone <repository-url>
cd cadoreadomicilio
```

2. Crea un ambiente virtuale Python:
```bash
python -m venv venv
source venv/bin/activate  # Su Linux/Mac
# oppure
venv\Scripts\activate  # Su Windows
```

3. Installa le dipendenze Python:
```bash
pip install -r requirements.txt
```

4. Esegui le migrazioni del database:
```bash
python manage.py migrate
```

5. Crea un superuser per l'admin (opzionale):
```bash
python manage.py createsuperuser
```

### Frontend Setup

1. Naviga nella cartella frontend:
```bash
cd frontend
```

2. Installa le dipendenze npm:
```bash
npm install
```

3. Compila il bundle JavaScript:
```bash
npm run build  # Per produzione
# oppure
npm run dev    # Per sviluppo
```

### Avvio del Server

```bash
python manage.py runserver
```

L'applicazione sarà disponibile all'indirizzo `http://localhost:8000`

## 📁 Struttura del Progetto

```
cadoreadomicilio/
├── cadoreadomicilio/          # Configurazione principale Django
│   ├── settings.py            # Impostazioni del progetto
│   ├── urls.py                # URL routing principale
│   └── wsgi.py                # WSGI configuration
├── locali/                    # App Django per la gestione dei locali
│   ├── models.py              # Modelli dei dati (Locale, ComuneConsegna)
│   ├── views.py               # API views
│   ├── serializers.py         # REST serializers
│   ├── forms.py               # Form per inserimento locali
│   └── templates/             # Template email
├── frontend/                  # App Django + React frontend
│   ├── src/                   # Codice sorgente React
│   │   ├── components/        # Componenti React
│   │   │   ├── App.js         # Componente principale
│   │   │   ├── collapsible.js # Lista collapsible dei locali
│   │   │   ├── select.js      # Filtri di selezione
│   │   │   └── emoji.js       # Icone emoji per categorie
│   │   └── index.js           # Entry point
│   ├── static/                # File statici compilati
│   ├── templates/             # Template HTML Django
│   └── package.json           # Dipendenze npm
├── manage.py                  # Django management script
└── requirements.txt           # Dipendenze Python
```

## 📊 Categorie Supportate

Il sistema supporta le seguenti categorie di attività:
- Abbigliamento
- Alimentari
- Articoli per animali
- Bar
- Cambio Gomme
- Edicola
- Fioreria
- Ferramenta e materiali edili
- Frutta e verdura
- Gelateria
- Libreria
- Macelleria
- Ottica
- Panificio
- Pizzeria
- Pasticceria
- Ristorante

## 🏘️ Comuni Coperti

Il servizio copre 20 comuni del Cadore (BL):
Auronzo, Borca, Calalzo, Cibiana, Comelico Superiore, Danta, Domegge, Lorenzago, Lozzo, Ospitale, Perarolo, Pieve, San Pietro, San Vito, Santo Stefano, Selva, Valle, Vigo, Vodo, Zoppè.

## 🔧 Configurazione

### Email Settings
Per abilitare le notifiche email, configurare le seguenti variabili in `settings.py`:
```python
EMAIL_HOST_USER = 'tuo-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tua-password'
```
**⚠️ IMPORTANTE**: Non committare mai credenziali reali nel repository!

### Database
Di default il progetto usa SQLite. Per passare a PostgreSQL o MySQL, modificare la sezione `DATABASES` in `settings.py`.

## 🌐 API Endpoints

- `GET /api/locali/` - Lista di tutti i locali (paginata, 20 per pagina)
- `GET /api/comuni/` - Lista di tutti i comuni di consegna

**Note:**
- Le API supportano paginazione: `?page=2`
- Rate limiting: 100 richieste/ora per utenti anonimi
- Formato: JSON

## 🐳 Docker Deployment

Il progetto include configurazione Docker completa:

```bash
# Quick start con Docker
docker-compose up -d
docker-compose exec web python manage.py migrate
```

Vedi [QUICKSTART.md](QUICKSTART.md) per dettagli completi.

## 📚 Documentazione Aggiuntiva

- **[QUICKSTART.md](QUICKSTART.md)** - Guida rapida per iniziare
- **[MIGLIORIE_IMPLEMENTATE.md](MIGLIORIE_IMPLEMENTATE.md)** - Lista completa delle migliorie implementate
- **[MIGLIORIE.md](MIGLIORIE.md)** - Suggerimenti per future migliorie

## 👥 Contribuire

Contributi, issues e feature requests sono benvenuti! Per suggerimenti o segnalazioni:
- Aprire una issue su GitHub
- Inviare una email a cadoreadomicilio@gmail.com

## 📝 Licenza

Questo progetto è stato sviluppato come iniziativa di supporto alla comunità locale del Cadore.

## 👤 Autore

Sviluppato da Andrea Barnabò
- Email: andrea.barnabo92@gmail.com

## 🙏 Ringraziamenti

Un ringraziamento a tutti i commercianti del Cadore che hanno aderito all'iniziativa e ai cittadini che supportano le attività locali.

---

**Nota**: Questo progetto è nato come risposta all'emergenza COVID-19 per supportare l'economia locale e facilitare l'accesso ai servizi essenziali.
