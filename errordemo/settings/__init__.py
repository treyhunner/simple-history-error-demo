from mixins.base import *

SECRET_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'app1',
    'app2',
)

TEST_RUNNER = 'errordemo.runner.BasicNoseRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
