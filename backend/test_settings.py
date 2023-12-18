from .settings import *


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "test_db",
        "NAME": "test_postgres",
        "USER": "test_postgres",
        "PASSWORD": "test_postgres",
        "PORT": 5432,
    }
}