BASE_DIR := $(CURDIR)
DOCKER_IMAGE_ANALYSIS := deep-metal-analysis
DOCKER_IMAGE_MODEL := deep-metal-model
DOCKER_IMAGE_DEMO := deep-metal-demo
GROUP_ID := 1000
USER_ID := 1000


.PHONY: analysis-build
analysis-build:
	docker build --rm -f docker/analysis/Dockerfile -t $(DOCKER_IMAGE_ANALYSIS) .


.PHONY: analysis-run
analysis-run:
	docker run --rm -it --shm-size=1024m -p 8080:8080 \
		-v $(CURDIR)/notebooks/analysis:/home/analysis/notebooks \
		-v $(CURDIR)/datasets:/home/analysis/datasets \
		$(DOCKER_IMAGE_ANALYSIS)


.PHONY: generator-build
generator-build:
	docker build --rm -f docker/deepmetal/Dockerfile \
		-t $(DOCKER_IMAGE_MODEL) .


.PHONY: generator-run
generator-run:
	docker run --gpus all --rm -it -p 8080:8080 \
		-u 1000 \
		-v $(CURDIR)/src/model:/home/deepmetal/model:rw \
		-v $(CURDIR)/datasets:/home/deepmetal/datasets:rw \
		$(DOCKER_IMAGE_MODEL)


.PHONY: generator-run-notebook
generator-run-notebook:
	docker run --gpus all --rm -it -p 8080:8080 \
		--shm-size=3096m \
		-u 1000 \
		-v $(CURDIR)/notebooks/deepmetal:/home/deepmetal/notebooks:rw \
		-v $(CURDIR)/src/model:/home/deepmetal/model:rw \
		-v $(CURDIR)/datasets:/home/deepmetal/datasets:rw \
		-v $(CURDIR)/resources:/home/deepmetal/resources:rw \
		$(DOCKER_IMAGE_MODEL)


.PHONY: demo-build
demo-build:
	docker build --no-cache --rm -f docker/demo/Dockerfile \
		--target backend-main \
		-t $(DOCKER_IMAGE_DEMO) .


.PHONY: demo-run
demo-run:
	docker run --rm -it -p 80:8080 \
		--env TOKENIZERS_PARALLELISM=true \
		$(DOCKER_IMAGE_DEMO)


.PHONY: demo-bash
demo-bash:
	docker run --rm -it -p 80:8080 \
		$(DOCKER_IMAGE_DEMO) /bin/bash


.PHONY: frontend-build
frontend-build:
	docker build --no-cache --rm -f docker/demo/Dockerfile \
		--target frontend-builder \
		-t deep-metal-frontend .

.PHONY: frontend-bash
frontend-bash:
	docker run --rm -it -p 80:5000 \
		deep-metal-frontend /bin/sh
