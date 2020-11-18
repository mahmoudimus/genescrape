FROM python:3
ENV LANG=C LC_ALL=C PYTHONUNBUFFERED=1
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
COPY ./scrapyd.conf /etc/scrapyd/
RUN RUN \
    DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install scrapyd \
    && apt-get clean autoclean \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/archives/*.deb \
    # Remove temporary files owned by root from the platformtemplate step
    && rm /tmp/* || true

ENTRYPOINT ["scrapyd"]
