"""
Impostazioni per testing.
"""
from .base import *

# Testing
DEBUG = True
SECRET_KEY = 'test-secret-key-not-for-production'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']

# Database in memoria per test veloci
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Email backend fittizio per test
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Password hasher veloce per test
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disabilita throttling nei test
REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = []

# Logging minimo per test
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'CRITICAL',
        },
    },
}
