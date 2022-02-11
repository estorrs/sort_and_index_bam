FROM ubuntu:18.04

RUN apt-get update && apt-get install -y vim wget curl git

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p /miniconda
ENV PATH="/miniconda/bin:$PATH"

# get env file seperately so it doesn't reinstall every time
COPY ./env.yaml /sort_and_index_bam/env.yaml
RUN conda env create --file /sort_and_index_bam/env.yaml 

COPY . /sort_and_index_bam

ENV PATH="/miniconda/envs/sort_and_index_bam/bin:$PATH"

CMD /bin/bash
