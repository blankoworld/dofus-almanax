NAME ?= dofus-almanax
VERSION ?= 0.2

build:
	docker build -t ${NAME}:${VERSION} .
