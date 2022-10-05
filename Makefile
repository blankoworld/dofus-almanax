NAME ?= dofus-almanax
VERSION ?= 0.1

build:
	docker build -t ${NAME}:${VERSION} .
