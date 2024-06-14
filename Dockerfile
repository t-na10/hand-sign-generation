FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    git \
    wget \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    libgdbm-dev \
    libdb-dev \
    uuid-dev \
    tar \
    libexpat1-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz \
    && tar -xvf Python-3.7.9.tgz
WORKDIR Python-3.7.9
RUN ./configure --enable-optimizations
RUN make -j$(nproc)
RUN make altinstall || { echo 'Build failed'; exit 1; }
WORKDIR /home
RUN python3.7 -m pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN yes | python3.7 -m pip install -r /tmp/requirements.txt
