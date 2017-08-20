PROJECT_ROOT=.
INSTALL_SCRIPT_PATH=$(PROJECT_ROOT)/install/install.sh

###############################################################################
# Utils targets
###############################################################################

hello-world:
	@$(INSTALL_SCRIPT_PATH) hello-world

print-current-path:
	@$(INSTALL_SCRIPT_PATH) print-current-path

print-project-name:
	@$(INSTALL_SCRIPT_PATH) print-project-name

###############################################################################
# Installation targets
###############################################################################

set-up-django:
	@$(INSTALL_SCRIPT_PATH) set-up-django

set-up-enviroment-vagrant:
	@$(INSTALL_SCRIPT_PATH) set-up-enviroment-vagrant

set-up-enviroment-virtualenv:
	@$(INSTALL_SCRIPT_PATH) set-up-enviroment-virtualenv
