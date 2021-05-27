# deep-metal
**Deep Metal**: when heavy metal meets data science. <br>
Text analysis of heavy metal lyrics and deep learning based lyrics generator.

<img src="./resources/presentation-pic.jpg" alt="deep-metal" />

## Legal notes

Due to incertainity about legal rights, I decided not to release a copy of the dataset used for this analysis. I hope you'll understand. The lyrics in question have been scraped from [DarkLyrics](http://www.darklyrics.com) with [this Python library](https://pypi.org/project/metalparser/).

## Requirements

Make sure you have a Python version >= 3.6 installed in your environment. To install all the required libraries just run:

```bash
pip install -r requirements.txt
```

## Contents

### Analysis notebooks

The analysis is divided in three Jupyter notebooks, stored in the `notebooks` folder:

- [Part I](https://github.com/lucone83/deep-metal/blob/master/notebooks/Dataset-analysis-part-I-general.ipynb) - Brief analysis of dataset contents: quantities (amount of artists, albums, album types, songs etc.) and simple statistics, album releases and distribution over the years,language distribution, bands popularity etc.
- [Part II](https://github.com/lucone83/deep-metal/blob/master/notebooks/Dataset-analysis-part-II-words-readability-metalness.ipynb) - Readability analysis: swear words ratio and Coleman-Liau grade index,
word frequence and definition of "metalness", POS analysis etc.
- [Part III](https://github.com/lucone83/deep-metal/blob/master/notebooks/Dataset-analysis-part-III-sentiment-genre_classification.ipynb) - Word based sentiment analysis, sentiment analysis with VADER, bands clustering based on sentiment and "metalness", bands emotional arcs, emotional arcs applied on literature, LDA topics modeling etc.

### Heavy metal lyrics generator

#### Model description

**DeepMetal** is a model capable of generating lyrics taylored for heavy metal songs.
The model is based on the [OpenAI GPT-2](https://huggingface.co/gpt2) and has been finetuned on a dataset of 141,718 heavy metal songs lyrics.

#### Intended uses and limitations

The model is released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0). You can use the raw model for lyrics generation or fine-tune it further to a downstream task.

#### How to use

The DVC repository for dataset and model is private, so it's not possible to download them using the commands in the `Makefile`. The model files have been released on [HuggingFace](https://huggingface.co/lucone83/deep-metal), together with related documentation and how-tos for using it with the HuggingFace `transformers` library.
If you want to use the model using the scripts stored in this repo, you need your system to be equipped with:

- Docker;
- The model files to be stored in `src/model/deepmetal`;

Then you can build and run the Docker image with this command:

```bash
make generator-build generator-run
```

Once in the container, you can launch the command:

```bash
./model/scripts/generate.sh
```

You can edit the `generate.sh` file in order to regulate the parameters for the generation.

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, it could be good to set a seed for reproducibility:

### Demo web application

I built a little SPA able to demonstrate some capabilities of the model.
You can find the related repository [here](https://github.com/lucone83/deep-metal-demo)


## About this project

Medium articles are available for each part of this project:

- **Part I**: https://blog.lucaballore.com/when-heavy-metal-meets-data-science-2e840897922e
- **Part II**: https://blog.lucaballore.com/when-heavy-metal-meets-data-science-3fc32e9096fa
- **Part III**: https://blog.lucaballore.com/when-heavy-metal-meets-data-science-episode-iii-9f6e4772847e

Any form of feedback is really appreciated :)
