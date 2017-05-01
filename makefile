build:
	docker build --tag todo:latest --file ./docker/tests.Dockerfile .

run:
	cd docker && \
	docker-compose build && \
	docker-compose up tests

test:
	cd docker && \
	docker-compose build && \
	docker-compose up tests

test_debugging_mode:
	# to debug using pdb/ipdb go in the docker-compose.yml file and uncomment
	# the stdin and tty lines in the *tests* service
	cd docker && \
	docker-compose build && \
	docker-compose up -d tests

docker_cleanup:
	cd docker && \
	docker-compose down --volumes 
