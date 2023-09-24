install:
	poetry install

start:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test -v2

coverage:
	poetry run coverage run manage.py test -v2 && poetry run coverage report