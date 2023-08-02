run: 
	python3 src/main.py

test:
	python3 -m pytest

install: 
	pip install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf /src/flask_app.egg-info

