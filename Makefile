include .env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' .env)

# standart commands for docker-compose managment
up:
	docker-compose up --remove-orphans --build
stop:
	docker-compose stop
down:
	docker-compose down --remove-orphans -v
logs:
	docker-compose logs -f

test:
	docker-compose run test

# comands for migration-container
msg?=
mgr:
	docker-compose run migration sh -c "alembic revision --autogenerate -m '$(msg)'"
	docker-compose run migration sh -c "alembic upgrade head"
	docker-compose stop migration
