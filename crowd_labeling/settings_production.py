from .settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.getcwd() + '/static'
