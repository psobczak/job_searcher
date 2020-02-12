FROM ubuntu:18.04

MAINTAINER <pawel.sobczak0@gmail.com>

WORKDIR /flask_client
COPY ./flask_client /flask_client

RUN apt-get update && apt-get install -fy --no-install-recommends \
    python3 \
    python3-setuptools \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install flask_pymongo flask

CMD ["python3", "app.py"]




