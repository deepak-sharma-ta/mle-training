FROM ubuntu:22.04
COPY . /app

ARG UNAME=john
# Add a new user "john" with user id 8877
RUN useradd --uid 8877 -m $UNAME && \
    apt-get update && \
    apt-get install -y wget libpq-dev python3-dev python3-pip sudo && \
    apt-get clean && \
    echo $UNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$UNAME \
    && chmod 0440 /etc/sudoers.d/$UNAME

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    -O ~/miniconda.sh && /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda update -n base -c defaults conda

# Change to non-root privilege
USER $UNAME