.PHONY: .pre-commit check_imports lint

.pre-commit: ## Check that pre-commit is installed
	@pre-commit -V || echo 'Please install pre-commit: https://pre-commit.com/'

check_imports:
	poetry run python ./scripts/find_and_check_imports.py langchain_contrasto

lint:
	poetry install --with lint --sync
	poetry run ruff format
	poetry run ruff check --fix