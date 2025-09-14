# Compiler and flags

UV := uv
PYTHON := python
RMDIR := rm -rf

SRC_DIR := src
TEST_DIR := tests
VENV_DIR := .venv

MAIN_PY := main.py

.PHONY: all build test clean

all: build

build:
	@if [ ! -d "$(VENV_DIR)" ]; then $(UV) venv; fi
	@$(UV) add --no-cache -r requirements.txt
	@$(UV) add --dev --no-cache -r dev-requirements.txt

test:
	@if [ -z "$(FILE)" ]; then $(UV) run $(PYTHON) -m unittest discover -v -s $(TEST_DIR) -p "*_test.py"; \
	else $(UV) run $(PYTHON) -m unittest -v $(TEST_DIR)/$$FILE; fi

# FIXME: This target currently does not work as expected
# run:
# 	@if [ -z "$(FILE)" ]; then FILE=$(MAIN_PY); fi; \
# 	$(UV) run $(FILE)

clean:
	@$(RMDIR) $(VENV_DIR) \
		$(SRC_DIR)/__pycache__ \
		$(TEST_DIR)/__pycache__
