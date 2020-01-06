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

COPY ./project /project

RUN conda env create -f /project/requirements.yml

ENV PATH /opt/conda/envs/tg-info/bin:$PATH
RUN sed '$ a source activate tg-info' -i /root/.bashrc

COPY ./scripts /scripts
RUN chmod +x /scripts/*

WORKDIR /project

EXPOSE 8000
EXPOSE 22