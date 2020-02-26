install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

start:
	poetry run gendiff ./tests/fixtures/before.json ./tests/fixtures/after.json
	poetry run gendiff ./tests/fixtures/before.yml ./tests/fixtures/after.yml
