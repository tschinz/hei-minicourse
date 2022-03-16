.PHONY: info conda-course-create conda-course-export conda-create conda-export clean view html htmlfull jupyter help

###########################################################################
# Detect OS                                                               #
###########################################################################
ifeq ($(OS),Windows_NT)
detected_OS := Windows
else
detected_OS := $(shell uname)
endif

###########################################################################
# GLOBALS                                                                 #
###########################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python
CONDA_ENV_NAME = jupyterbook-env
CONDA_ENV_FILE = jupyterbookenv.yml

CONDA_COURSE_ENV_NAME = minicourse
CONDA_COURSE_ENV_FILE = condaenv.yml

###########################################################################
# OS Specifics                                                            #
###########################################################################
ifeq ($(detected_OS),Windows)
	PDFVIEWER = 'start "" /max'
ifeq (,$(shell where conda))
	HAS_CONDA = False
else
	HAS_CONDA = True
	SEARCH_ENV = $(shell conda.bat info --envs | grep $(CONDA_ENV_NAME))
	FOUND_ENV_NAME = $(word 1, $(notdir $(SEARCH_ENV)))
	# check if conda environment is active
ifneq ($(CONDA_DEFAULT_ENV),$(FOUND_ENV_NAME))
	CONDA_ACTIVATE := source $$(conda.bat info --base)/etc/profile.d/conda.sh ; conda activate $(CONDA_ENV_NAME)
else
	CONDA_ACTIVATE := true
endif
endif
endif

ifeq ($(detected_OS),Darwin)
	PDFVIEWER = open
ifeq (,$(shell which conda))
	HAS_CONDA = False
else
	HAS_CONDA = True
	ENV_DIR = $(shell conda info --base)
	MY_ENV_DIR = $(ENV_DIR)/envs/$(CONDA_ENV_NAME)
	CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate $(CONDA_ENV_NAME)
endif
endif

ifeq ($(detected_OS),Linux)
	PDFVIEWER = xdg-open
ifeq (,$(shell which conda))
	HAS_CONDA = False
else
	HAS_CONDA = True
	ENV_DIR = $(shell conda info --base)
	MY_ENV_DIR = $(ENV_DIR)/envs/$(CONDA_ENV_NAME)
	CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate $(CONDA_ENV_NAME)
endif
endif

###########################################################################
# COMMANDS                                                                #
###########################################################################
info: ## Information about the environemnt
	@echo "Environment Informations"
	@echo "  * Detected OS: $(detected_OS)"
	@echo "  * Pdfviewer: $(PDFVIEWER)"
	@echo "  * Conda found: $(HAS_CONDA)"
	@echo "  * Conda envfile: $(CONDA_ENV_FILE)"
	@echo "  * Conda dir: $(ENV_DIR)"
	@echo "  * Conda envdir: $(MY_ENV_DIR)"

conda-course-create: ## Install conda environment
ifeq (True,$(HAS_CONDA))
ifneq ("$(wildcard $(MY_ENV_DIR))","") # check if the directory is there
	@echo ">>> Found $(CONDA_COURSE_ENV_NAME) environment in $(MY_ENV_DIR). Skipping installation..."
else
	@echo ">>> Detected conda, but $(CONDA_COURSE_ENV_NAME) is missing in $(ENV_DIR). Installing ..."
	@conda env create -f $(CONDA_COURSE_ENV_FILE) -n $(CONDA_COURSE_ENV_NAME)
endif
else
	@echo ">>> Install conda first."
	exit
endif

conda-course-export: ## export conda environment
	@conda env export > $(CONDA_COURSE_ENV_FILE)
	@echo ">>> Conda environment '$(CONDA_COURSE_ENV_NAME)' exported."

conda-create: ## Install conda environment
ifeq (True,$(HAS_CONDA))
ifneq ("$(wildcard $(MY_ENV_DIR))","") # check if the directory is there
	@echo ">>> Found $(CONDA_ENV_NAME) environment in $(MY_ENV_DIR). Skipping installation..."
else
	@echo ">>> Detected conda, but $(CONDA_ENV_NAME) is missing in $(ENV_DIR). Installing ..."
	@conda env create -f $(CONDA_ENV_FILE) -n $(CONDA_ENV_NAME)
endif
else
	@echo ">>> Install conda first."
	exit
endif

conda-export: ## export conda environment
	@conda env export > $(CONDA_ENV_FILE)
	@echo ">>> Conda environment '$(CONDA_ENV_NAME)' exported."

html: ## build jupyterbook html files
	@$(CONDA_ACTIVATE) && cd jupyterbook && jupyter-book build .
	@echo ">>> Build Jupyterbook"

htmlfull: clean ## build from scratch jupyterbook html files
	@$(CONDA_ACTIVATE) && cd jupyterbook && jupyter-book build .
	@echo ">>> Build Jupyterbook"

view: ## view html files
	@$(PDFVIEWER) jupyterbook/_build/html/index.html &
	@echo ">>> Open Jupyterbook"

clean: ## clen generated file
	@rm -R jupyterbook/_build
	@echo ">>> Removed jupyterbook/_build/ folder"

jupyter: ## start jupyterlab instance
	@$(CONDA_ACTIVATE) && jupyter lab --app_dir=./jupyterbook

help: ## Show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; \
	{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
