build:
	docker build -t todo:latest -f ./docker/tests.Dockerfile .

run:
	cd docker && \
	docker-compose build && \
	docker-compose up tests

run_tests:
	cd docker && \
	docker-compose build && \
	docker-compose up tests

docker_cleanup:
	cd docker && \
	docker-compose down -v && \
	docker rmi -f $(docker images -f dangling=true -q) && \
	docker images | grep "pattern" | awk '{print $1}' | xargs docker rm
