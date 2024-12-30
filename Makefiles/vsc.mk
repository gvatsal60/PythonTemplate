include Makefiles/rules.mk

# Targets
.PHONY: all build test clean

all: build

build:
	@$(BUILD_CMD)

test:
	@$(TEST_CMD)

run:
	@$(RUN_CMD)

clean:
	@$(CLEAN_CMD)
