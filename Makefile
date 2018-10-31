CWD=$(shell pwd)
SERVICE=example

init:
	python3 -m metaendpoints.tools.esp_init

esp:
	python3 -m metaendpoints.tools.esp_deploy --service=$(SERVICE) --lang=python --workdir=$(CWD)

dev:
	python3 -m metaendpoints.tools.esp_dev --service=$(SERVICE)
