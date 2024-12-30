# Targets
.PHONY: all test clean

PYTHON_CMD := python3
BUILD_TOOL_CMD := $(PYTHON_CMD) -m
BUILD_CMD := $(BUILD_TOOL_CMD) build
TEST_CMD := $(BUILD_TOOL_CMD) test
RUN_CMD := $(BUILD_TOOL_CMD) run
CLEAN_CMD := rm -rf .mypy_cache/ .venv/