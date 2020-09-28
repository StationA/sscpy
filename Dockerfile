FROM stationa/ssc:alpine

RUN apk add --no-cache \
    ca-certificates \
    wget \
    build-base \
    libffi-dev \
    python3 \
    python3-dev

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

# Add sscpy sources and install

ADD . /sscpy

WORKDIR /sscpy

RUN pip3 install --upgrade pip
RUN pip3 install tox
RUN pip3 install .
