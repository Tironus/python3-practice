install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=paramiko/tests paramiko/tests/testCommandGenerator.py

lint:
	pylint --disable=R,C,E1120 paramiko/commandGenerator.py
	pylint --disable=R,C,E1120 paramiko/configCommander.py
	pylint --disable=R,C,E1120 paramiko/deviceCommander.py

all:
	install lint test