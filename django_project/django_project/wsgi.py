import os
from os.path import abspath, dirname, join, normpath, basename

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_NAME = basename(DJANGO_ROOT)

ENV_FILE = normpath(join(PROJECT_ROOT, 'conf/.env'))
load_dotenv(ENV_FILE)


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      PROJECT_NAME + '.settings')
application = get_wsgi_application()
