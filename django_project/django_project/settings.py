from os.path import abspath, dirname, basename

PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_NAME = basename(DJANGO_ROOT)
