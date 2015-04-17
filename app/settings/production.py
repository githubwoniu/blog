from .base import *

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'MHuRtn7J1C',
        'HOST': 'LOCALHOST',
        'PORT': '',
    }
}


ALLOWED_HOSTS = [
        '127.0.0.1',
        'leonardo.do',
        '.leonardo.do',
        '104.236.61.48',
        ]
