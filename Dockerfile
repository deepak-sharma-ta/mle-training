FROM ubuntu:22.04 as builder
COPY . /app

ARG UNAME=john
# Add a new user "john" with user id 8877
RUN useradd --uid 8877 -m $UNAME && \
    apt-get update && \
    apt-get install -y wget libpq-dev python3-dev python3-pip sudo && \
    apt-get clean && \
    echo $UNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$UNAME \
    && chmod 0440 /etc/sudoers.d/$UNAME

FROM continuumio/miniconda3

COPY --from=builder /app /app

RUN conda env create -f app/deploy/conda/linux_cpu_py310.yml
RUN echo "source activate mle-dev-docker" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

WORKDIR /app

# # Change to non-root privilege
USER $UNAME