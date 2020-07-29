create-network:
	docker network create django-blog > /dev/null 2>&1

start-service:
	docker-compose up -d

stop-service:
	docker-compose down

restart-service:
	make start-service
	make stop-service

create-superuser:
	docker exec -it django-blog python /code/Dblog/manage.py createsuperuser