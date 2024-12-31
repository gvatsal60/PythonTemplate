# Compiler and flags

PYTHON := python3

SRC_DIR := src
TEST_DIR := tests
VENV_DIR := .venv

ifeq ($(OS), Windows_NT)
	RMDIR:=rmdir /s /q
	VENV_PYTHON:=.\.venv\Scripts\python.exe
else
	RMDIR:=rm -rf
	VENV_PYTHON:=./.venv/bin/python
endif

BUILD_PY_ENV := activate.py
MAIN_PY := main.py

.PHONY: all build test clean

all: build

build:
	@echo "Building project..."
	@$(PYTHON) $(BUILD_PY_ENV)

test:
	@echo "Building tests..."

run:
	@echo "Running project..."
	@if [ -z "$(FILE)" ]; then \
		FILE=$(MAIN_PY); \
	fi; \
	$(VENV_PYTHON) $(SRC_DIR)/$$FILE

clean:
	@echo "Cleaning project..."
	@$(RMDIR) $(VENV_DIR) $(SRC_DIR)/*.pyc $(SRC_DIR)/*.pyo \
		$(SRC_DIR)/*.pyd $(SRC_DIR)/*.pyw \
		$(SRC_DIR)/*.pyz $(SRC_DIR)/*.pyzw
