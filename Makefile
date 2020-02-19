install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run gendiff before.json after.json