BASE_DIR := $(CURDIR)
DOCKER_IMAGE := transcoder
DATASETS_FOLDER := $(CURDIR)/datasets
DATASETS_URL := https://storage.googleapis.com/deep-metal-data/datasets/deep-metal-datasets.zip


##############################
# Data
##############################
.PHONY: download-datasets
download-datasets:
	mkdir -p $(DATASETS_FOLDER)
	wget $(DATASETS_URL) -P $(DATASETS_FOLDER)
	unzip -d $(DATASETS_FOLDER) $(DATASETS_FOLDER)/deep-metal-datasets.zip
	rm $(DATASETS_FOLDER)/deep-metal-datasets.zip
