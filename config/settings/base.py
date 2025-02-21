from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(os.path.join(BASE_DIR, "tmp/secrets.json")) as f:
    secrets_json = json.loads(f.read())


def get_secret(setting, secrets=secrets_json):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable.".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
    'solo.apps.SoloAppConfig',
    'imagefit',
    'tinymce',
    'apps.training.apps.TrainingConfig',
    'apps.team.apps.TeamConfig',
    'apps.customer.apps.CustomerConfig',
    'apps.frontend.apps.FrontendConfig',
    'apps.pages.apps.PagesConfig',
    'apps.settings.apps.SettingsConfig',
    'request'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'request.middleware.RequestMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tmp/db.sqlite3'),
    }
}

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


LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/admin/login/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/dist')]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'tmp/static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp/media/')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

IMAGEFIT_ROOT = os.path.join(BASE_DIR, 'tmp')

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
    "valid_classes": "",
    "valid_styles": {
        '*': 'color,text-align,padding-left,text-decoration,background-color'
    },
    "advlist_bullet_styles": "default",
    "advlist_number_styles": "default"
}

DEFAULT_FROM_EMAIL = get_secret('DEFAULT_FROM_EMAIL')

PROTECTED = get_secret('PROTECTED')

SITE_ID = 1
