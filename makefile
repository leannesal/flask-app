run: 
	python3 project/src/main.py

test:
	python3 -m pytest

install: 
	pip install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf project/src/flask_app.egg-info

