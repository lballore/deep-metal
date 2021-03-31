BASE_DIR := $(CURDIR)
DOCKER_IMAGE_ANALYSIS := deep-metal-analysis
DOCKER_IMAGE_MODEL := deep-metal-model
GROUP_ID := 1000
USER_ID := 1000


.PHONY: analysis-build
analysis-build:
	docker build --rm -f docker/analysis/Dockerfile -t $(DOCKER_IMAGE_ANALYSIS) .


.PHONY: analysis-run
analysis-run:
	docker run --rm -it -p 8080:8080 \
		-v notebooks/analysis:/home/analysis/notebooks \
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
