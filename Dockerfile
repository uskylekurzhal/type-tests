FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y install --no-install-recommends \
    python2.7-dev \
    python-pip \

    python3.7 \
    python3.7-dev \
    python3-pip

RUN pip install --no-cache-dir \
    typing

RUN pip3 install --no-cache-dir \
    mypy

WORKDIR /app