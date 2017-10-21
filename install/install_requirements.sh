#!/bin/bash
# These scripts could be or coudn't not be executed in a enviroment or not
# that's why this instalations goes in this file.

if [ ! "$BASH_VERSION" ] ; then
    echo "This code should be executed with bash, use 'bash ./$0' or"\
      "'bash $0' instead"
    exit 0
fi

INSTALL_PATH=$(dirname $(realpath -s $0))
ROOT_PATH=$(dirname $INSTALL_PATH)
DJANGO_ROOT=$PROJECT_ROOT/$PROJECT_NAME/

###############################################################################
# Installation functions
###############################################################################

function install-pip-requirements {
  print 'Installing pip requirements'
  pip install -r $INSTALL_PATH/requirements.txt
}

function install-pip-requirements-in-virtualenv {
  start-env
  print 'Installing pip requirements'
  pip install -r $INSTALL_PATH/requirements.txt
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
