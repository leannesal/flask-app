SRC_DIR := src
IMAGE_REG ?= ghcr.io
IMAGE_REPO ?= leannesal/flask-app
IMAGE_TAG ?= latest

run: 
	python3 src/main.py

test: venv  ## Unit tests for Flask app
	. $(SRC_DIR)/.venv/bin/activate \
	&& pytest -v


install: 
	pip install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

image:  #Build container image from Dockerfile 
	docker build . --file Dockerfile \
	--tag $(IMAGE_REG)/$(IMAGE_REPO):$(IMAGE_TAG)

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf /src/flask_app.egg-info



# ============================================================================

venv: $(SRC_DIR)/.venv/touchfile

$(SRC_DIR)/.venv/touchfile: $(SRC_DIR)/requirements.txt
	python3 -m venv $(SRC_DIR)/.venv
	. $(SRC_DIR)/.venv/bin/activate; pip install -r $(SRC_DIR)/requirements.txt
	touch $(SRC_DIR)/.venv/touchfile


