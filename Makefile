DOCKER_COMPOSE := docker-compose


upd:
	${DOCKER_COMPOSE} up -d
down:
	${DOCKER_COMPOSE} down
db_migrate:
	${DOCKER_COMPOSE} run web flask db migrate
db_upgrade:
	${DOCKER_COMPOSE} run web flask db upgrade
