#!/bin/bash

if [ ! "$BASH_VERSION" ] ; then
    echo "This code should be executed with bash, use 'bash ./$0' or"\
      "'bash $0' instead"
    exit 0
fi

# Constants
INSTALL_PATH=$(dirname $(realpath -s $0))
ROOT_PATH=$(dirname $INSTALL_PATH)
DJANGO_ROOT=$PROJECT_ROOT/$PROJECT_NAME/
CONF_FOLDER=$PROJECT_ROOT/conf/

# LOAD .env variables into this bash script
# user variables as any other for example if you have a env variable called
# PROJECT_NAME you can access it from this script like any other variable
# echo $PROJECT_NAME
PIP_FOLDER=venv
source $CONF_FOLDER/.env

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

###############################################################################
# Clean functions
###############################################################################

function clean-venv {
  print 'Uninstalling venv'
  sudo pip3 uninstall virtualenv
  print 'Removing virtualenv directory'
  rm -R ./$PIP_FOLDER/
  rm venv
}


###############################################################################
# Installation functions
###############################################################################

# This should go in another script that could be or coudn't not be executed
# in a enviroment.
#function install-pip-requirements {
#  print 'Installing pip requirements'
#  pip install -r $INSTALL_PATH/requirements.txt
#}

# This should go in another script that could be or coudn't not be executed
#function install-dependencies {
#  install-pip-requirements
#}

############### General
function before-install {
  sudo apt-get autoremove && apt-get update
}

function install-python {
  sudo apt-get install python3.5 python3-pip python3-dev
}

# deprecated function
function change-django-project-name {
  PROJECT_NAME=django_project
  if [ ! -d $PROJECT_ROOT/$PROJECT_NAME/ ]; then
    mv $PROJECT_ROOT/django_project/django_project/ \
      $PROJECT_ROOT/django_project/$PROJECT_NAME
    mv $PROJECT_ROOT/django_project/ $PROJECT_ROOT/$PROJECT_NAME
  fi
}

function set-up-django: {
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

############### Vagrant

function install-vagrant-requirements {
  vagrant plugin install dotenv
}

function install-vagrant-with-virtualbox {
  echo 'vagrant==1:1.9.7'
  echo 'virtualbox==5.0.40'
  sudo apt-get install vagrant=1:1.9.7 virtualbox=5.0.40*
}

###############################################################################
# Set-up functions
###############################################################################

function set-up-enviroment-virtualenv {
  before-install
  install-python
  install-virtualenv
  set-up-django
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
