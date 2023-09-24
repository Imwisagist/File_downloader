from os import getenv, path
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv('SECRET_KEY', 'secret-keygsdfgGFGDGFDG#%$@#23342')

DEBUG = getenv('DEBUG') == 'True'

DOCKER = getenv('DOCKER') == 'True'

ALLOWED_IMAGE_EXTENTIONS = ('jpg', 'jpeg', 'png')

ALLOWED_TEXT_EXTENTIONS = ('txt', 'docx')

ALLOWED_EXTENTIONS = (
    *ALLOWED_IMAGE_EXTENTIONS,
    *ALLOWED_TEXT_EXTENTIONS,
)

REDIS_HOST = 'redis'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ('application/json',)

if DOCKER:  # pragma: no cover
    CELERY_BROKER_URL = "redis://redis:6380/0"
    CELERY_RESULT_BACKEND = "redis://redis:6380/0"
else:
    CELERY_BROKER_URL = "redis://localhost:6380/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6380/0"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'api.apps.ApiConfig',
]

ALLOWED_HOSTS = ('*',)

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'
STATIC_ROOT = path.join(BASE_DIR, 'static') 

LANGUAGE_CODE = 'ru'

# Default settings under this line
#######################################################################

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
