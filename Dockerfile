FROM ubuntu:22.04
COPY . /app

RUN apt-get update && \
    apt-get install -y wget libpq-dev python3-dev python3-pip && \
    apt-get clean

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    -O ~/miniconda.sh && /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda update -n base -c defaults conda
