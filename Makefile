format:
	ruff format .; ruff check . --fix
	rm requirements.txt && poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev
	yamlfmt .
	mbake format Makefile

lint:
	ruff check . && ruff check . --diff
	mypy -p statbov -m manage -p tests
	radon cc ./statbov -a -na
	rm requirements.txt && poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev
	yamlfmt -lint .
	mbake format --check Makefile

run:
	python manage.py runserver

test:
	ruff check . && ruff check . --diff
	mypy -p statbov -m manage -p tests
	radon cc ./statbov -a -na
	export POSTGRES_HOST="localhost" && pytest -s -x --cov=statbov -vv
	coverage html
	rm requirements.txt && poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev

functional-test:
	export POSTGRES_HOST="localhost" && pytest -m "functional_test"

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

update:
	poetry update
	rm requirements.txt && poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev
	python scripts/update_chromedriver.py

chromedriver:
	python scripts/update_chromedriver.py

.PHONY: format lint run test functional-test migrations migrate update chromedriver