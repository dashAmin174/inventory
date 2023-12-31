from pathlib import Path
import os


CSRF_TRUSTED_ORIGINS = ["https://dashamin174-jubilant-space-spork-pjprv55gr4gf7q4x-8005.preview.app.github.dev"]

SECRET_KEY = "django-insecure-cnvj_6xqst#5dhxc1-3^cm06kd7ap81&wr8s@_#)jvju(k6w9v"

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# STATIC FILES (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# STATIC FILES DIRS
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Manifest Static Files Storage is recommended in production, to prevent outdated
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# static root Dir configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

# STATIC URL
STATIC_URL = '/static/'

# Media root Dir configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Media URL
MEDIA_URL = 'media/'