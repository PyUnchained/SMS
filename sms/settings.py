"""
Django settings for sms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#Finds the path to settings.py
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


#Finds the path to the folder containing settings.py, then creates an absolute path
#to the folder containing settings.py
PROJECT_PATH = os.path.join(BASE_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

#Main template directory
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)


#Select where the root media folder is
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2)*y2251m_mlq1e#p%5q$xkjru^jgp1x3e0jk5w^n$83n=bo1i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'office',
    'sms_admin',
    'msg_box',
    'cal',
    'autofixture',
    'gem_soft',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sms.urls'

WSGI_APPLICATION = 'sms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smsdb2',
        'USER': 'tatenda',
        'PASSWORD': 'devcrm',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


#Since the static files are all stored in one place (given that many apps use
#the exact same files) this is required for the collectstatic command to find
#them
STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'static'),)


STATIC_URL = '/static/'


#Settings required in order for logging in and out to work properly
LOGIN_URL = '/'