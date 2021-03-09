FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install python3.7 python3-pip python3-tk tmux
RUN rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 0
RUN update-alternatives --set python /usr/bin/python3.7

COPY docker/deepmetal/requirements.txt /tmp/requirements.txt

RUN groupadd -r -g 1000 deepmetal
RUN useradd -m -u 1000 -g 1000 -d /home/deepmetal deepmetal
RUN python -m pip install --upgrade pip

USER deepmetal

ENV PATH "/home/deepmetal/.local/bin:${PATH}"
RUN python -m pip install --user -r /tmp/requirements.txt

WORKDIR /home/deepmetal

CMD [ "/bin/bash" ]
