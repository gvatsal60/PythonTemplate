# Compiler and flags

UV := uv
PYTHON := python
RMDIR := rm -rf

SRC_DIR := src
TEST_DIR := tests
VENV_DIR := .venv

MAIN_PY := main.py

export UV_LINK_MODE := copy

.PHONY: all build test clean

all: build

build:
	@$(UV) add --no-cache

test:
	@if [ -z "$(FILE)" ]; then $(UV) run $(PYTHON) -m unittest discover -v -s $(TEST_DIR) -p "*_test.py"; \
	else $(UV) run $(PYTHON) -m unittest -v $(TEST_DIR)/$$FILE; fi

clean:
	@$(RMDIR) $(VENV_DIR)
	@find $(SRC_DIR) $(TEST_DIR) -type d -name '__pycache__' -prune -exec $(RMDIR) {} +
