FROM stationa/ssc:latest

RUN apk add --no-cache \
    build-base \
    python3 \
    python3-dev \
    py-pip \
    zlib-dev \
    lzo-dev \
    libxml2-dev \
    libffi-dev

# Add sscpy sources and install

ADD . /sscpy

WORKDIR /sscpy

RUN pip3 install --upgrade pip
RUN pip3 install tox
RUN pip3 install .
