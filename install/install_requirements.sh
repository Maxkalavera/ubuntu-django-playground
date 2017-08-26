# These scripts could be or coudn't not be executed in a enviroment or not
# that's why this instalations goes in this file.

PROJECT_ROOT=.
INSTALL_FOLDER=$PROJECT_ROOT/install/
DJANGO_ROOT=$PROJECT_ROOT/$PROJECT_NAME/

###############################################################################
# Installation functions
###############################################################################

function install-pip-requirements {
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
}

function install-pip-requirements-in-virtualenv {
  start-env
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
  finish-env
}

function install-dependencies {
  install-pip-requirements
}

###############################################################################
# test functions
###############################################################################

function test-uwsgi {
  uwsgi --http :8000 --wsgi-file $PROJECT_ROOT/test/uwsgi_test.py
}
