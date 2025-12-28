ruff:
	ruff check --fix --show-fixes .
	ruff format --exclude migrations .

lint: ruff
