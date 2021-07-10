"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.test.utils import ignore_warnings


ignore_warnings(message="No directory at", module="whitenoise.base").enable()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k_5=$toy!c6ejh@qa0tl2)fv%$9kt=0154460ifil^d18h%*^*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False



ALLOWED_HOSTS = ['*']


SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    #local
    'blog.apps.BlogConfig',
    'django.contrib.sites', 
    'django.contrib.sitemaps',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    #downloaded
    'bootstrap4',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hidden_place.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'hidden_place.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#DATE_FORMAT = "d-m-Y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#перенаправление зарегистрированного пользоватедя
#LOGIN_REDIRECT_URL = 'dashboard'

#юрл для входа
#LOGIN_URL = 'login'

#юрл для выхода
#LOGOUT_URL = 'logout'



#email

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ehgwrabbit@gmail.com' 
EMAIL_HOST_PASSWORD = '$6120$x326y457z628a45b$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#файлы для загрузки
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
     #'account.authentication.EmailAuthBakend',
     #'social_core.backends.facebook.FacebookOAuth2',
     #'social_core.backends.twitter.TwitterOAuth',
     #social_core.backends.google.GoogleOAuth2',
]

'''
SOCIAL_AUTH_FACEBOOK_KEY = '515954923051860'
SOCIAL_AUTH_FACEBOOK_SECRET = 'afd745c0c7d72f1259b5926550a8ecc7'

#SOCIAL_AUTH_TWITTER_KEY =
#SOCIAL_AUTH_TWITTER_SECRET =
'''