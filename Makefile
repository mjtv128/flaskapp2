install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_application.py

lint:
	pylint --disable=R,C app.py

deploy:
	echo "Deploying app"
	eb deploy hello-env

all: install lint test

run: 
	python app.py