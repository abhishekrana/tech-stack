# syntax=docker/dockerfile:1.3

ARG VARIANT=22.04
FROM ubuntu:${VARIANT}

ENV BUILD_CACHE=1 \
    COMPOSE_DOCKER_CLI_BUILD=1 \
    DOCKER_BUILDKIT=1 \
    SHELL=/bin/bash

# Add sudo
RUN apt-get update \
    && apt-get install -y --no-install-recommends sudo \
    && sudo apt-get autoremove -y && sudo apt-get clean -y && sudo rm -rf /var/lib/apt/lists/*

# Install utilities
RUN sudo apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && yes | sudo unminimize 2>&1 \
    && sudo apt-get -y install \
    apt-transport-https \
    bash-completion \
    build-essential \
    gcc \
    ca-certificates \
    curl \
    dnsutils \
    git \
    htop \
    httpie \
    iputils-ping \
    jq \
    locales \
    locate \
    lsof \
    nano \
    net-tools \
    openssh-client \
    pkg-config \
    postgresql-client \
    procps \
    python3-pip \
    software-properties-common \
    ssh-client \
    tar \
    tree \
    unzip \
    vim \
    wget \
    yamllint \
    && sudo apt-get autoremove -y && sudo apt-get clean -y && sudo rm -rf /var/lib/apt/lists/*

# Set locale
RUN sudo bash -c 'echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen' \
    && sudo locale-gen

# Disable 'Please select the geographic area in which you live' prompt
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install python
ARG PYTHON_VERSION=3.11
RUN sudo apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && sudo add-apt-repository ppa:deadsnakes/ppa \
    && sudo apt-get install -y --no-install-recommends python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python${PYTHON_VERSION}-venv \
    && sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 100 \
    && sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 110 \
    && sudo apt-get autoremove -y && sudo apt-get clean -y && sudo rm -rf /var/lib/apt/lists/*

# Install poetry
ARG POETRY_VERSION=1.5.1
ENV PIP_DEFAULT_TIMEOUT=60 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir poetry==${POETRY_VERSION}

# Install go
ARG GO_VERSION=1.21.0
RUN cd /tmp \
    && wget --progress=dot:giga https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz \
    && sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz \
    && echo "export PATH=${PATH}:/usr/local/go/bin" >> ~/.bashrc \
    && rm -rf go${GO_VERSION}.linux-amd64.tar.gz
ENV PATH="$PATH:/usr/local/go/bin"

# Install node
ARG NODE_VERSION="18"
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | sudo -E bash - && \
    sudo apt-get install -y nodejs

# Install npm
ARG NPM_VERSION="9.8.1"
RUN sudo npm install -g npm@${NPM_VERSION}

# Install task
ARG TASK_VERSION="v3.28.0"
RUN sudo bash -c "$(curl --location https://taskfile.dev/install.sh)" -- -b /usr/local/bin/ -d ${TASK_VERSION} \
    && sudo wget -O /usr/share/bash-completion/completions/task.bash https://raw.githubusercontent.com/go-task/task/${TASK_VERSION}/completion/bash/task.bash

WORKDIR /workspace
