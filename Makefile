PROJECT_ROOT=.
INSTALL_SCRIPT_PATH=$(PROJECT_ROOT)/install/install.sh

print-current-path:
	@$(INSTALL_SCRIPT_PATH) print-current-path

print-project-name:
	@$(INSTALL_SCRIPT_PATH) print-project-name

create-django-project:
	@$(INSTALL_SCRIPT_PATH) create-django-project

set-up-enviroment-vagrant:
	@$(INSTALL_SCRIPT_PATH) set-up-enviroment-vagrant

set-up-enviroment-virtualenv:
	@$(INSTALL_SCRIPT_PATH) set-up-enviroment-virtualenv

hello-world:
	@$(INSTALL_SCRIPT_PATH) hello-world
