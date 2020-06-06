import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import random

from IPython.display import display, HTML, Markdown
from wordcloud import WordCloud


COLORS = [
    'yellowgreen',
    'red',
    'gold',
    'lightskyblue',
    'lightcoral',
    'blue',
    'darkgreen',
    'yellow',
    'grey',
    'violet',
    'magenta',
    'cyan'
]


def printmd(string):
    display(Markdown(string))


def plot_pie_graph(x, y, figsize, labels, labeldistance, pctdistance=1.0, shadow=False, title=''):
    porcent = ((100.* y) / y.sum())
    random.shuffle(COLORS)

    plt.figure(figsize=figsize)
    plt.title = title
    patches, texts = plt.pie(y, startangle=90, radius=1.2, colors=COLORS[:len(labels)])
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
    plt.legend(
        patches,
        labels,
        loc='best',
        bbox_to_anchor=(-0.1, 1.),
        fontsize=10,
        shadow=shadow
    )

    plt.show()


def plot_vertical_bars(df, x, xlabel, y, ylabel, figsize, title, display_values=True, legend=False):
    ax = df.plot.bar(
        x=x,
        y=y,
        figsize=figsize,
        title=title,
        legend=legend)
    ax.set_xlabel(xlabel, labelpad=10)
    ax.set_ylabel(ylabel, labelpad=10)

    if(display_values):
        rects = ax.patches
        values = [ str(rect.get_height()) for rect in rects ]
        for rect, label in zip(rects, values):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                rect.get_height() + 10,
                label,
                ha='center',
                va='bottom',
                rotation=90
            )


def plot_horizontal_bars(df, x, xlabel, y, ylabel, figsize, title, display_values=True, values_offset=None, legend=False):
    ax = df.plot.barh(
        x=x,
        y=y,
        figsize=figsize,
        title=title,
        legend=legend
    )
    ax.set_xlabel(xlabel, labelpad=10)
    ax.set_ylabel(ylabel, labelpad=10)

    if(display_values):
        rects = ax.patches
        values = [ str(rect.get_width()) for rect in rects ]
        for rect, label in zip(rects, values):
            ax.text(
                rect.get_width() + values_offset,
                rect.get_y() + .15 - (rect.get_height() / 2),
                label,
                ha='center',
                va='bottom'
            )


def plot_scatter(df, x, xlabel, y, ylabel, figsize, title, labels, fontsize=16):
    fig, ax = plt.subplots(figsize=figsize)
    plt.title = title

    df.plot(
        kind="scatter",
        x=x,
        y=y,
        ax=ax
    )
    for i, point in df.iterrows():
        ax.text(
            point[x],
            point[y],
            str(point[labels]),
            fontsize=fontsize
        )

    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)

    plt.show()


def plot_wordcloud(words, width, height, figsize, scale, max_words=500, filename=None):
    wordcloud = WordCloud(
        width=width,
        height=height,
        max_words=max_words,
        scale=scale,
    )
    wordcloud.generate_from_frequencies(dict(words))

    plt.figure(figsize=figsize)
    plt.imshow(wordcloud)
    plt.axis("off")

    if filename is not None:
        plt.savefig(filename, bbox_inches='tight')

    plt.show()


def plot_connected_scatter(data, x, xlabel, y, ylabel, figsize, legend=None, annotation_field=None, linestyle='-', marker='o'):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlabel(xlabel, labelpad=10, fontsize=15)
    ax.set_ylabel(ylabel, labelpad=10, fontsize=15)

    for df in data:
        plt.plot(list(df[x]), list(df[y]), linestyle=linestyle, marker=marker)
        if annotation_field:
            for i, txt in enumerate(list(df[annotation_field])):
                ax.annotate(txt, (list(df[x])[i], list(df[y])[i]), fontsize=15)

    if legend:
        ax.legend(legend, loc="best")

    plt.show()


def plot_3d_scatter(x, y, z, xlabel, ylabel, zlabel, figsize, annotations):
    fig, ax = plt.subplots(figsize=figsize)
    ax = plt.gca(projection="3d")
    ax.set_xlabel(xlabel, labelpad=10, fontsize=10)
    ax.set_ylabel(ylabel, labelpad=10, fontsize=10)
    ax.set_zlabel(zlabel, labelpad=10, fontsize=10)

    ax.scatter(x, y, z, c='r', s=100)
    ax.plot(x, y, z, color='r')

    for i, txt in enumerate(annotations):
        ax.text(x[i], y[i], z[i], txt, fontsize=10)

    plt.show()
