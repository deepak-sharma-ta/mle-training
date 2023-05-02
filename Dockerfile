FROM continuumio/miniconda3
ARG UNAME=john
COPY . /app

RUN conda env create -f app/deploy/conda/linux_cpu_py310.yml

RUN useradd -ms /bin/bash $UNAME 
RUN usermod -aG sudo $UNAME 

RUN chown -R $UNAME:$UNAME /app

# # Change to non-root privilege
USER $UNAME

RUN echo "source activate mle-dev-docker" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

WORKDIR /app