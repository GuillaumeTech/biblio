
dev:
	echo "todo"

build:
	echo "todo"

start:
	echo "todo"

dev-db:
	docker run --name biblio-db -e POSTGRES_PASSWORD=biblio-dev-pass -e POSTGRES_DB=biblio -d -p 5432:5432 postgres 

migrate-last:
	poetry run alembic upgrade head

new-migration:
	echo "todo"