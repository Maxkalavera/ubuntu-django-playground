#!/bin/bash

PROJECT_ROOT=.
# some variables are taken of this env file, for example PROJECT_NAME  can
# be found here.
ENV_PATH=$PROJECT_ROOT/conf/.env
source $ENV_PATH

INSTALL_FOLDER=$PROJECT_ROOT/install/
DJANGO_ROOT=./$PROJECT_NAME/

###############################################################################
# Utils
###############################################################################

function start-env {
  source ./$PIP_FOLDER/bin/activate
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

function print-current-path {
  print $PWD
}

function print-project-name {
  print $PROJECT_NAME
}

###############################################################################
# Clean functions
###############################################################################

function clean-venv {
  print 'Desinstalando venv'
  sudo pip3 uninstall virtualenv
  print 'Eliminando virtualenv directory'
  rm -R ./$PIP_FOLDER/
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
  virtualenv $PIP_FOLDER --no-site-packages
  print 'Creating symlink venv to virtualenv/bin/activate'
  ln -s $PROJECT_ROOT/$PIP_FOLDER/bin/activate $PROJECT_ROOT/env
}

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

function install-vagrant-with-virtualbox {
  # vagrant==1:1.9.7
  # virtualbox==5.0.40
  sudo apt-get install vagrant=1:1.9.7 virtualbox=5.0.40*
}

function create-django-project {
  django-admin.py $PROJECT_NAME
}

function set-up-enviroment-vagrant {
  before-install
  install-python
  install-vagrant-with-virtualbox
}

function set-up-enviroment-virtualenv {
  before-install
  install-python
  install-virtualenv
  install-pip-requirements-in-virtualenv
}

function install-dependencies {
  install-pip-requirements
}

# Call function from arguments
$*
