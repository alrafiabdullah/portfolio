"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import socket
import os
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
REACT_DIR = os.path.join(BASE_DIR, 'build')
REACT_STATIC_DIR = os.path.join(BASE_DIR, 'build/static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT_DIR = os.path.join(BASE_DIR, 'staticfiles')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

if os.path.exists('secrets.json'):
    with open('secrets.json') as secret:
        data = json.load(secret)
        SECRET_KEY = data["DJANGO_SECRET_KEY"]
    secret.close()

GOOGLE_RECAPTCHA_SECRET_KEY = data["GOOGLE_RECAPTCHA"]

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == "Grenade":
    DEBUG = True
    ALLOWED_HOSTS = ["127.0.0.1", ]
else:
    DEBUG = False
    ALLOWED_HOSTS = ["alrafi-portfolio.herokuapp.com", ]

EMAIL_HOST = data["EMAIL_HOST"]
EMAIL_HOST_USER = data["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = data["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = data["EMAIL_PORT"]
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, REACT_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': data["NAME"],
        'USER': data["USER"],
        'PASSWORD': data["PASSWORD"],
        'HOST': data["HOST"],
        'PORT': data["PORT"]
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = [
    STATIC_DIR,
    REACT_STATIC_DIR
]

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_ROOT_DIR
MEDIA_ROOT = os.path.join(REACT_STATIC_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',)
}
