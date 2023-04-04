.PHONY: create-network build-python run-postgresql run-python stop-postgresql clean

PORT ?= 5432

# Target for stopping all running Docker containers
clean:
	docker rm -f $$(docker ps -aq)

# Check if the IMAGE variable is set
ifeq ($(strip $(IMAGE)),)
	$(error IMAGE is not set)
endif

create-network:
	docker network inspect pandas_showroom >/dev/null 2>&1 || docker network create pandas_showroom

pylint:
	docker run -it --rm \
	-v "${PWD}/$(IMAGE)":/app \
	"$(IMAGE)" \
	pylint --rcfile=/app/.pylintrc /app

# Target for building Docker image
build-python:
	docker build --progress=plain --no-cache -t "$(IMAGE)" ${PWD}/$(IMAGE)

# Target for running Docker container in the background and exposing port 5432
run-postgresql: create-network
	docker run -d -p $(PORT):5432 --net pandas_showroom --name postgresql $(IMAGE)

run-python: create-network
	docker run -it -rm \
	--net pandas_showroom \
	-v "${PWD}/data_inputs/":"/inputs" \
	-v "${PWD}/data_outputs/":"/outputs" \
	-v "${PWD}/secrets":/secrets \
	-v "${PWD}/$(IMAGE)":/app \
	"$(IMAGE)"

# Target for stopping specific Docker container and removing it
stop-postgresql:
	docker stop $(IMAGE)
	docker rm $(IMAGE)
