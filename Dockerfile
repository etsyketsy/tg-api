FROM continuumio/miniconda:4.4.10

RUN apt-get update && apt-get install -qqy \
    wget \
    bzip2 \
    libssl-dev \
    openssh-server \
    python3-dev \
    default-libmysqlclient-dev \
    gcc

RUN mkdir -p /project | \
    mkdir -p /media


COPY ./project/requirements.yml /project/requirements.yml

RUN conda env create -f /project/requirements.yml

COPY . .

WORKDIR /project