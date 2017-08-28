PROJECT_ROOT=.
INSTALL_ENVIRONMENT_SCRIPT=$(PROJECT_ROOT)/install/install_environment.sh
INSTALL_REQUIREMENTS_SCRIPT=$(PROJECT_ROOT)/install/install_requirements.sh

###############################################################################
# Utils targets
###############################################################################

hello-world:
	@$(INSTALL_ENVIRONMENT_SCRIPT) hello-world

print-current-path:
	@$(INSTALL_ENVIRONMENT_SCRIPT) print-current-path

print-project-name:
	@$(INSTALL_ENVIRONMENT_SCRIPT) print-project-name

###############################################################################
# Installation targets
###############################################################################

set-up-django:
	@$(INSTALL_ENVIRONMENT_SCRIPT) set-up-django

set-up-enviroment-vagrant:
	@$(INSTALL_ENVIRONMENT_SCRIPT) set-up-enviroment-vagrant

set-up-enviroment-virtualenv:
	@$(INSTALL_ENVIRONMENT_SCRIPT) set-up-enviroment-virtualenv

install-dependencies:
	@$(INSTALL_REQUIREMENTS_SCRIPT) install-dependencies
