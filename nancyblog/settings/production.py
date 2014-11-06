from .base import *
import os

# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False


# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True


# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql development headers)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['NLB_DB_NAME'],
        'USER': os.environ['NLB_DB_USER'],
        'PASSWORD': os.environ['NLB_DB_PWD'],
'HOST': '',  # Set to empty string for localhost.
'PORT': '',  # Set to empty string for default.
'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}


# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'nancyblog',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }


try:
    from .local import *
except ImportError:
    pass
