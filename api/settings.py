"""Django settings for api project.
"""

#
# Imports
#
import os

import api.sensitive_settings

#
# Sensitive settings
#
ALLOWED_HOSTS = api.sensitive_settings.ALLOWED_HOSTS
DATABASES = api.sensitive_settings.DATABASES
SECRET_KEY = api.sensitive_settings.SECRET_KEY
EMAIL_HOST = api.sensitive_settings.EMAIL_HOST
EMAIL_PORT = api.sensitive_settings.EMAIL_PORT
EMAIL_HOST_USER = api.sensitive_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = api.sensitive_settings.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = api.sensitive_settings.EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = api.sensitive_settings.DEFAULT_FROM_EMAIL
SERVER_EMAIL = api.sensitive_settings.SERVER_EMAIL

#
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#
# Project's root directory
#
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#
# Debug mode:
#
DEBUG = True

#
# Application definition
#
INSTALLED_APPS = [
    #
    # Grappelli admin
    #
    'grappelli.dashboard',
    'grappelli',

    #
    # Django applications
    #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #
    # Third party applications
    #
    'admin_honeypot',
    'rest_framework',

    #
    # api project's applications
    #
    'api.applications.login.apps.LoginConfig',
    'api.applications.workspace.apps.WorkspaceConfig',
    'api.applications.membership.apps.MembershipConfig',
    'api.applications.product.apps.ProductConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #
    # LOD middleware
    #
    'api.middlewares.lod.apps.LodMiddleware',
]

#
# A string representing the full Python import path to the root URLconf
#
ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api.wsgi.application'

#
# Password validation
#
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

#
# Internationalization
#
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#
# Static files (CSS, JavaScript, Images)
#
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

AUTH_USER_MODEL = 'login.Login'

#
# Grappelli settings
#
GRAPPELLI_INDEX_DASHBOARD = 'api.grappelli_dashboard.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = "LOD"

#
# Django honeypot
#
ADMINS = [
    ('Thierry', 'mail@thierry-decker.com'),
]
ADMIN_HONEYPOT_EMAIL_ADMINS = True
