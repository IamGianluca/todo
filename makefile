build:
	docker build --tag todo:latest --file ./docker/app.Dockerfile .

run:
	cd docker && \
	docker-compose build && \
	docker-compose up app

test:
	cd docker && \
	docker-compose build && \
	docker-compose up tests && \
	docker-compose down

test_interactive_mode:
	cd docker && \
	docker-compose build && \
	docker-compose run tests wait-for-it.sh app:5000 -- pytest -s

docker_cleanup:
	cd docker && \
	docker-compose down --volumes
