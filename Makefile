install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test_a:
	poetry run pytest -vv

start:
	poetry run gendiff ./tests/fixtures/before.json ./tests/fixtures/after.json
	poetry run gendiff ./tests/fixtures/before.yml ./tests/fixtures/after.yml

start_advanced:
	poetry run gendiff ./tests/fixtures/advanced_before.json ./tests/fixtures/advanced_after.json
	poetry run gendiff ./tests/fixtures/advanced_before.yml ./tests/fixtures/advanced_after.yml

publish:
	poetry publish -r test
