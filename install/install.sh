#!/bin/bash
PROJECT_ROOT=.
PIP_PROJECT_NAME=venv
INSTALL_FOLDER=$PROJECT_ROOT/install/

PROJECT_NAME=blog
DJANGO_ROOT=./$PROJECT_NAME/

###############################################################################
# Utils
###############################################################################

function create-django-project {
  django-admin.py $PROJECT_NAME
}

function start-env {
  source ./$PIP_PROJECT_NAME/bin/activate
}

function finish-env {
  deactivate
}

function hello-world {
  print 'Hello word!'
}

function print {
  echo -e '\n'$1
}

###############################################################################
# Clean functions
###############################################################################

function clean-venv {
  print 'Desinstalando venv'
  sudo pip3 uninstall virtualenv
  print 'Eliminando virtualenv directory'
  rm -R ./$PIP_PROJECT_NAME/
  rm venv
}

###############################################################################
# test functions
###############################################################################

function test-uwsgi {
  uwsgi --http :8000 --wsgi-file $PROJECT_ROOT/test/uwsgi_test.py
}

###############################################################################
# Installation functions
###############################################################################

function before-install {
  sudo apt-get autoremove && apt-get update
}

function install-python {
  sudo apt-get install python3.5 python3-pip python3-dev
}

function install-virtualenv {
  print 'Instaling virtualenv'
  pip3 install virtualenv
  print 'Starting the venv project'
  virtualenv $PIP_PROJECT_NAME --no-site-packages
  print 'Creating symlink venv to virtualenv/bin/activate'
  ln -s $PROJECT_ROOT/$PIP_PROJECT_NAME/bin/activate $PROJECT_ROOT/venv
}

function install-pip-requirements {
  start-env
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
  finish-env
}

function install-pip-requirements-in-virtualenv {
  start-env
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
  finish-env
}

function all() {
  before-install
  install-python
  install-virtualenv
  #install-pip-requirements
  install-pip-requirements-in-virtualenv
}

# Call function from arguments
$*
