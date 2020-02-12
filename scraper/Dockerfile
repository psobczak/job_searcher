FROM ubuntu:18.04

MAINTAINER <pawel.sobczak0@gmail.com>

WORKDIR /scraper
COPY ./scraper /scraper

RUN apt-get update && apt-get install -fy --no-install-recommends \
    python3 \
    python3-setuptools \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install wheel && \
    pip3 install -r requirements.txt

CMD ["python3", "main.py"]








