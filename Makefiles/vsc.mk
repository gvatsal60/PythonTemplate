include cfg/.env
include Makefiles/rules.mk

# Targets
.PHONY: all test clean

all: run

test:
	@$(TEST_CMD)

run:
	@$(RUN_CMD)

clean:
	@$(CLEAN_CMD)
