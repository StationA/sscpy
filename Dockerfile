FROM stationa/ssc:latest as ssc

FROM python:alpine

COPY --from=ssc /usr/local/lib/libssc.so /usr/local/lib/libssc.so
COPY --from=ssc /usr/local/include/sscapi.h /usr/local/include/sscapi.h

RUN apk add --no-cache \
    ca-certificates \
    build-base \
    libffi-dev

# Add sscpy sources and install

ADD . /sscpy

WORKDIR /sscpy

RUN pip3 install .

# Test sscpy
RUN python3 /sscpy/examples/pvwatts.py /sscpy/examples/ca_weather.csv
