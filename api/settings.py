"""Django settings for api project.
"""

#
# Imports
#
import os

#
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#
# SECURITY WARNING: keep the secret key used in production secret!
#
SECRET_KEY = 'v8kt6jdbd2!!9!08der(@6k+fsb=qn6yv1xep_%pw7vlw@_x+p'

#
# Debug mode:
#
DEBUG = True

#
# Allowed host:
#
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

#
# Application definition
#
INSTALLED_APPS = [
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
    # api project's applications
    #
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
# Database
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lod',
        'USER': 'lod_backend',
        'PASSWORD': 'zvxmhwfn',
        'HOST': 'localhost',
        'PORT': '',
    }
}

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
STATIC_URL = '/static/'
