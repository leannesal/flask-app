run: 
	python3 project/src/main.py

install: 
	pip install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf project/flask_app.egg-info