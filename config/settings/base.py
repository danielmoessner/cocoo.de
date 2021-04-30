from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import json
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Secret settings
with open(os.path.join(BASE_DIR, "tmp/secrets.json")) as f:
    secrets_json = json.loads(f.read())


def get_secret(setting, secrets=secrets_json):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable.".format(setting)
        raise ImproperlyConfigured(error_msg)


# Security (keep the secret key used in production secret!)
SECRET_KEY = get_secret('SECRET_KEY')

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'solo.apps.SoloAppConfig',
    'imagefit',
    'tinymce',
    'apps.training.apps.TrainingConfig',
    'apps.team.apps.TeamConfig',
    'apps.customer.apps.CustomerConfig',
    'apps.frontend.apps.FrontendConfig',
    'apps.pages.apps.PagesConfig',
    'apps.settings.apps.SettingsConfig',
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

ROOT_URLCONF = 'config.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tmp/db.sqlite3'),
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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Login
LOGIN_URL = '/admin/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/dist')]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'tmp/static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp/media/')

# Imagefit
IMAGEFIT_ROOT = os.path.join(BASE_DIR, 'tmp')

# TinyMCE
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": False,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
               "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
               "code,help,wordcount",
    "toolbar": "undo redo | formatselect | "
               "bold italic underline | forecolor backcolor | alignleft aligncenter "
               "alignright alignjustify | bullist numlist outdent indent | link",
    "block_formats": 'Paragraph=p; Überschrift=h3; Unterüberschrift=h4; Vorformatiert=pre',
    "invalid_styles": 'font-family font-size font-weight',
    "valid_classes": "",
    "advlist_bullet_styles": "default",
    "advlist_number_styles": "default"
}

# E-Mail
EMAIL_USE_TLS = True
EMAIL_HOST = get_secret('EMAIL_HOST')
EMAIL_HOST_USER = get_secret('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PWD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = get_secret('DEFAULT_FROM_EMAIL')
