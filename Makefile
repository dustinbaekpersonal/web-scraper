pip-tools-dev:
	pip install pip-tools>=7.0.0 setuptools>=68.0.0
	pip-compile requirements/test.in && pip-compile requirements/dev.in
	pip-sync requirements/dev.txt