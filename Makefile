
up:
	docker-compose up -d --build

down:
	docker-compose down --rmi all -v --remove-orphans