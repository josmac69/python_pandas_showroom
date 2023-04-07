ifdef_check = $(if $(SCRIPT),,@echo "SCRIPT variable is not set or empty"; exit 1)

.PHONY: create-network \
	build-pandas-image build-jupyter-image \
	run-python run-jupyter \
	run-postgresql stop-postgresql \
	clean pylint \
	delete-pandas-images delete-jupyter-images delete-dangling-images

PORT ?= 5432
PANDAS_IMAGE ?= python_pandas_showroom
JUPYTER_IMAGE ?= jupyter_pandas_showroom
POSTGRESQL_IMAGE ?= adventureworks

# Target for stopping all running Docker containers
clean:
	docker rm -f $$(docker ps -aq)

create-network:
	docker network inspect pandas_showroom >/dev/null 2>&1 || docker network create pandas_showroom

pylint:
	$(call ifdef_check)
	docker run -it --rm \
	-v "${PWD}/$(SCRIPT)":/app \
	"$(PANDAS_IMAGE)" \
	pylint --rcfile=/app/.pylintrc /app

# Target for building Docker image
build-pandas-image:
	docker build --progress=plain --no-cache -t "$(PANDAS_IMAGE)" -f Dockerfile.python_pandas_showroom .

build-jupyter-image:
	docker build --progress=plain --no-cache -t "$(JUPYTER_IMAGE)" -f Dockerfile.jupyter_pandas_showroom .

# Target for running Docker container in the background and exposing port 5432
run-postgresql: create-network
	docker run -d -p $(PORT):5432 --net pandas_showroom --name postgresql $(POSTGRESQL_IMAGE)

run-python: create-network
	$(call ifdef_check)
	docker run -it --rm \
	--net pandas_showroom \
	-v "${PWD}/data_inputs/":"/inputs" \
	-v "${PWD}/data_outputs/":"/outputs" \
	-v "${PWD}/secrets":/secrets \
	-v "${PWD}/$(SCRIPT)":/app \
	"$(PANDAS_IMAGE)"

run-jupyter:
	docker run -i -t \
	-v ${PWD}/jupyter_notebooks:/opt/notebooks \
	-v ${PWD}/data_inputs:/inputs \
	-v ${PWD}/data_outputs:/outputs \
	-p 8888:8888 \
	"$(JUPYTER_IMAGE)" /bin/bash \
	-c "/opt/conda/bin/conda install jupyter -y --quiet && \
	/opt/conda/bin/jupyter notebook \
	--notebook-dir=/opt/notebooks --ip='*' --port=8888 \
	--no-browser --allow-root"

# Target for stopping specific Docker container and removing it
stop-postgresql:
	docker stop $(POSTGRESQL_IMAGE)
	docker rm $(POSTGRESQL_IMAGE)

delete-pandas-image:
	docker images | awk '/^$$(PANDAS_IMAGE)/ {print $$3}' | xargs -I {} docker rmi {}

delete-jupyter-image:
	docker images | awk '/^$$(JUPYTER_IMAGE)/ {print $$3}' | xargs -I {} docker rmi {}

delete-dangling-images:
	docker images -f "dangling=true" -q | xargs -I {} docker rmi {}
