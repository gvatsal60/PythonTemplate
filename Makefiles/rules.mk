# Targets
.PHONY: all test clean

BUILD_TOOL_CMD := make -j$(shell nproc) -C $(TOP_DIR)
TEST_CMD := $(BUILD_TOOL_CMD) test
RUN_CMD := $(BUILD_TOOL_CMD) run
CLEAN_CMD := $(BUILD_TOOL_CMD) clean