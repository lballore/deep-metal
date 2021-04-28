FROM python:3.7.9-slim-buster

COPY docker/analysis/requirements.txt /tmp/requirements.txt

RUN groupadd -r -g 1000 analysis
RUN useradd -m -u 1000 -g 1000 -d /home/analysis analysis
RUN python -m pip install --upgrade pip

USER analysis

ENV PATH "/home/analysis/.local/bin:${PATH}"
RUN python -m pip install --user -r /tmp/requirements.txt

WORKDIR /home/analysis

CMD [ "jupyter-notebook", ".", "--ip=0.0.0.0", "--port=8080" ]
