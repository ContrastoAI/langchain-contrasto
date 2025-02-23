.PHONY: check_imports lint

check_imports:
	poetry run python ./scripts/find_and_check_imports.py langchain_contrasto

lint:
	poetry install --include lint --sync
	poetry run ruff format --check
	poetry run ruff check