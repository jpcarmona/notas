# -*- coding: utf-8 -*-
"""
Django settings for notas project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch,PosixGroupType
AUTHENTICATION_BACKENDS = (
'django_auth_ldap.backend.LDAPBackend',
'django.contrib.auth.backends.ModelBackend',
)

import ConfigParser
c = ConfigParser.ConfigParser()
c.read('notas.cfg')

AUTH_LDAP_SERVER_URI = c.get('ldap','AUTH_LDAP_SERVER_URI')
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_DN_TEMPLATE = c.get('ldap','AUTH_LDAP_USER_DN_TEMPLATE')

AUTH_LDAP_CONNECTION_OPTIONS = {
ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": c.get('ldap','AUTH_LDAP_GROUP_ACTIVE')
    "is_staff": c.get('ldap','AUTH_LDAP_GROUP_STAFF')
    "is_superuser": c.get('ldap','AUTH_LDAP_GROUP_SUPERUSER')
}
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(c.get('ldap','AUTH_LDAP_GROUP_SEARCH'),
        ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
    }
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1#t-j2julyvxiquduj-)h7c#z^=gscazhaeq8+uaixrd=jre0k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'notas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
            # Put strings here, like "/home/html/static" or "C:/www/django/static".
            # Always use forward slashes, even on Windows.
            # Don't forget to use absolute paths, not relative paths.
            os.path.join(BASE_DIR,"static"),
                )


if DEBUG:
    import logging, logging.handlers
    logfile = "/tmp/django-ldap-debug.log"
    my_logger = logging.getLogger('django_auth_ldap')
    my_logger.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(
       logfile, maxBytes=1024 * 500, backupCount=5)

    my_logger.addHandler(handler)

from django.contrib import admin
admin.site.site_header="Gonzalo Nazareno - Notas"
admin.site.index_title="Notas"

