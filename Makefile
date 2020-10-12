install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=configCommander testConfigCommander.py

lint:
	pylint --disable=R,C,E1120 commandGenerator.py
	pylint --disable=R,C,E1120 configCommander.py
	pylint --disable=R,C,E1120 deviceCommander.py

format:
	black *.py

all:
	install lint test