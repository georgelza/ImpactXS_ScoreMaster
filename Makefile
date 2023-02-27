# https://www.youtube.com/watch?v=w2UeLF7EEwk

.ONESHELL:

.DEFAULT_GOAL := run

PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip

venv/bin/activate: requirements
	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	$(PYTHON) main.py

upgrade:
	pip install --upgrade pip

clean:
	rm -rf __pychche__
	rm -rf venv

.PHONY: run clean