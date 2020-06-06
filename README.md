# deep-metal
**Deep Metal**: when heavy metal meets data science. <br>
Text analysis of heavy metal lyrics and NN-based lyrics generator (WIP).

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

Work in progress.

## About this project

Medium articles are available for each part of this project:

- **Part I**: https://medium.com/@luca.ballore/when-heavy-metal-meets-data-science-2e840897922e
- **Part II**: https://medium.com/@luca.ballore/when-heavy-metal-meets-data-science-3fc32e9096fa
- **Part III**: https://medium.com/@luca.ballore/when-heavy-metal-meets-data-science-episode-iii-9f6e4772847e

Any form of feedback is really appreciated :)
