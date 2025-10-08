"""
Settings package per gestire ambienti diversi.

Per usare un ambiente specifico, impostare la variabile d'ambiente:
DJANGO_SETTINGS_MODULE=cadoreadomicilio.settings.production
DJANGO_SETTINGS_MODULE=cadoreadomicilio.settings.development
"""

# Import automatico basato su DJANGO_ENV
import os

env = os.environ.get('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
elif env == 'test':
    from .test import *
else:
    from .development import *
