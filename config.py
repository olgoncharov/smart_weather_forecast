import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(BASE_DIR, 'geo_objects.sqlite')

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300
