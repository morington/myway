import random
import string

import structlog
from pathlib import Path

from confhub.reader import ReaderConf

logger: structlog.BoundLogger = structlog.get_logger('settings')
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=120))


__config = ReaderConf('config/settings.yml', 'config/.secrets.yml', dev=False)
config = __config.data

REMEMBER_TIME = config.get('webapp', {}).get('REMEMBER_TIME')

#  DEBUG MODE
DEBUG = config.get('webapp', {}).get('DEBUG')
logger.debug('Reading settings...', debug_mode=DEBUG)

#  HOSTS
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0', 'http://127.0.0.1', 'http://localhost']

#  STATICS
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / config.get('webapp', {}).get('ROOT_STATIC_DIR')

#  MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / config.get('webapp', {}).get('ROOT_MEDIA_DIR')

#  LANGUAGE
LANGUAGE_CODE = 'ru-RU'

#  I18N
TIME_ZONE = config.get('webapp', {}).get('TIME_ZONE', 'UTC')
USE_I18N = False
USE_TZ = True

#  AUTH
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'users:login'
LOGIN_URL = 'users:login'

#  OTHER
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'webapp.User'

#  OTHER SETTINGS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'src.authentication.apps.AuthConfig',
    'src.webapp.apps.WebappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'myway_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / config.get('webapp', {}).get('ROOT_TEMPLATES_DIR')],
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

WSGI_APPLICATION = 'myway_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config.get('postgresql', {}).get('scheme'),
        'NAME': config.get('postgresql', {}).get('path'),
        'USER': config.get('postgresql', {}).get('user'),
        'PASSWORD': config.get('postgresql', {}).get('password'),
        'HOST': config.get('postgresql', {}).get('host'),
        'PORT': config.get('postgresql', {}).get('port'),
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
