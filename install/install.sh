#!/bin/bash

# Constants
PROJECT_ROOT=.
INSTALL_FOLDER=$PROJECT_ROOT/install/
DJANGO_ROOT=./$PROJECT_NAME/

PIP_FOLDER=venv

# Global variables
project_name=

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
  output=maxkalavera
  sed -i 's/cosa/'$output'/g' stuff.txt
  cat stuff.txt
  print 'Hello word!'
}

function print {
  echo -e '\n'$1
}

function print-current-path {
  print $PWD
}

function get-project-name {
  if [ -d $PROJECT_ROOT/django_project/ ]; then
    option=n
    while [ $option != y ]; do
      echo 'Enter the name to set to your django project:'
      read project_name
      echo 'Are you sure you want to use $project_name as your project name? y/n'
      read option
    done
  fi
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

# This should go in another script that could be or coudn't not be executed
# in a enviroment.
function test-uwsgi {
  uwsgi --http :8000 --wsgi-file $PROJECT_ROOT/test/uwsgi_test.py
}

###############################################################################
# Installation functions
###############################################################################

# This should go in another script that could be or coudn't not be executed
# in a enviroment.
function install-pip-requirements {
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
}

# This should go in another script that could be or coudn't not be executed
function install-dependencies {
  install-pip-requirements
}

############### General
function before-install {
  sudo apt-get autoremove && apt-get update
}

function install-python {
  sudo apt-get install python3.5 python3-pip python3-dev
}

function set-up-django: {
  get-project-name
  if [ -d $PROJECT_ROOT/django_project/ ]; then
    sed -i 's/django_project.settings/'$project_name'.settings/g' \
      $PROJECT_ROOT/django_project/manage.py
    sed -i 's/django_project.settings/'$project_name'.settings/g' \
      $PROJECT_ROOT/django_project/django_project/wsgi.py
    mv $PROJECT_ROOT/django_project/django_project/ \
      $PROJECT_ROOT/django_project/$project_name
    mv $PROJECT_ROOT/django_project/ $PROJECT_ROOT/$project_name
  fi
}

# in a enviroment.
############### Virtualenv
function install-virtualenv {
  print 'Instaling virtualenv'
  pip3 install virtualenv
  print 'Starting the venv project'
  virtualenv $PIP_FOLDER --no-site-packages
  print 'Creating symlink venv to virtualenv/bin/activate'
  ln -s $PROJECT_ROOT/$PIP_FOLDER/bin/activate $PROJECT_ROOT/env
}

function install-pip-requirements-in-virtualenv {
  start-env
  print 'Installing pip requirements'
  pip install -r $INSTALL_FOLDER/requirements.txt
  finish-env
}

function set-up-enviroment-virtualenv {
  before-install
  install-python
  install-virtualenv
  install-pip-requirements-in-virtualenv
  set-up-django
}

############### Vagrant
function install-vagrant-with-virtualbox {
  # vagrant==1:1.9.7
  # virtualbox==5.0.40
  sudo apt-get install vagrant=1:1.9.7 virtualbox=5.0.40*
}

function set-up-enviroment-vagrant {
  before-install
  install-python
  install-vagrant-with-virtualbox
  set-up-django
}

###############################################################################
# Main
###############################################################################

# Call function from arguments
$1
