.PHONY: all lint flake8 tests setup

ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
COVERAGE = venv/Scripts/coverage.exe
PTEST = venv/Scripts/pytest.exe
else
PYTHON = ./venv/bin/python
COVERAGE = ./venv/bin/coverage
PTEST = ./venv/bin/pytest
endif

SOURCE = tester_flask
TESTS = tests

PYLINT = $(PYTHON) -m pylint
FLAKE8 = $(PYTHON) -m flake8
PEP257 = $(PYTHON) -m pep257
PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered
PIP = $(PYTHON) -m pip install

all: tests

flake8:
	$(FLAKE8) $(SOURCE)
	$(FLAKE8) $(TESTS)/test

lint:
	$(PYLINT) $(TESTS)/test
	$(PYLINT) $(SOURCE)

pep257:
	$(PEP257) --match='.*\.py' $(TESTS)/test
	$(PEP257) $(SOURCE)

tests: flake8 pep257 lint
	$(PYTEST) --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

setup: setup_python setup_pip

setup2: setup_python2 setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt
	$(PIP) -r deploy.txt
	$(PIP) -r $(TESTS)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv

setup_python2:
	$(PYTHON_BIN) -m pip install virtualenv
	$(PYTHON_BIN) -m virtualenv ./venv
