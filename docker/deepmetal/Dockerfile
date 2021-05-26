FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install python3 python3-pip python3-tk tmux
RUN rm -rf /var/lib/apt/lists/
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY docker/deepmetal/requirements.txt /tmp/requirements.txt

RUN groupadd -r -g 1000 deepmetal
RUN useradd -m -u 1000 -g 1000 -d /home/deepmetal deepmetal

USER deepmetal

ENV PATH "/home/deepmetal/.local/bin:${PATH}"
RUN pip install --user -r /tmp/requirements.txt

WORKDIR /home/deepmetal

CMD [ "/bin/bash" ]
