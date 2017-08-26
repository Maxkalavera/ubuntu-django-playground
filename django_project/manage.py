#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname, join, normpath, basename

from dotenv import load_dotenv

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
DJANGO_ROOT = dirname(abspath(__file__))
PROJECT_NAME = basename(DJANGO_ROOT)

ENV_FILE = normpath(join(PROJECT_ROOT, 'conf/.env'))
load_dotenv(ENV_FILE)



if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          PROJECT_NAME + '.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                'Couldn\'t import Django. Are you sure it\'s installed and '
                'available on your PYTHONPATH environment variable? Did you '
                'forget to activate a virtual environment?'
            )
        raise
    execute_from_command_line(sys.argv)
