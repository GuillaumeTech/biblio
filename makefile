
dev:
	poetry run uvicorn main:app --reload

setup-dev: dev-db migrate-last dev-db-populate

build:
	echo "todo"

start:
	echo "todo"

dev-db:
	docker run --name biblio-db -e POSTGRES_PASSWORD=biblio-dev-pass -e POSTGRES_DB=biblio -d -p 5432:5432 postgres 

dev-db-populate:
	poetry run python scripts/populate_db.py

migrate-last:
	poetry run alembic upgrade head

new-migration:
	echo "todo"