FROM python:3.8-slim
COPY . /genescrape/crawler
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
WORKDIR /genescrape/crawler

RUN pip install -r requirements.txt