"""
Impostazioni per ambiente di sviluppo.
"""
from .base import *

# DEBUG attivo in sviluppo
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

# Database SQLite per sviluppo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Email backend console per sviluppo (stampa email in console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging dettagliato per sviluppo
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'locali': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Disabilita throttling in sviluppo
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': '10000/hour',
    'user': '10000/hour'
}
