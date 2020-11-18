FROM python:3
ENV LANG=C LC_ALL=C PYTHONUNBUFFERED=1
COPY . /genescrape/crawler
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
VOLUME /genescrape/crawler
WORKDIR /genescrape/crawler

RUN \
    DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g \
    libtiff5-dev \
    libfreetype6-dev \
    libwebp-dev \
    libopenjp2-7-dev \
    && pip install -r requirements.txt \
    && apt-get clean autoclean \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/archives/*.deb \
    # Remove temporary files owned by root from the platformtemplate step
    && rm /tmp/* || true