FROM python:3.8-slim
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
COPY ./scrapyd.conf /etc/scrapyd/
RUN pip install scrapyd

ENTRYPOINT ["scrapyd"]
