FROM stationa/ssc:latest

RUN apk add --no-cache \
    build-base \
    python2 \
    python2-dev \
    py2-pip \
    zlib-dev \
    lzo-dev \
    libxml2-dev \
    libffi-dev

# Add sscpy sources and install

ADD . /sscpy

WORKDIR /sscpy

RUN pip install .
