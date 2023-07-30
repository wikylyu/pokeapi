from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "pokeapi_db",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
        "CONN_MAX_AGE": 30,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DEBUG = True
TASTYPIE_FULL_DEBUG = True
