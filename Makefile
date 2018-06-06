
create-virtualenv:
	virtualenv -p python3 .env

pip-install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

loaddata:
	python manage.py loaddata books.json

createsuperuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic

runserver:
	python manage.py runserver 0.0.0.0:8080
