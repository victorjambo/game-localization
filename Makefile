build:
	docker-compose build

start:
	docker-compose up web

build-test:
	docker-compose build test

test:
	docker-compose run test

migrate:
	docker compose run web flask db upgrade

volume:
	docker volume create db_data
