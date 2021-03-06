# -*- coding: utf-8 -*-

import datetime
import re
import time

import scrapy
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst


class OrphanetCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    orphan = scrapy.Field()
    name = scrapy.Field()
    synonyms = scrapy.Field()
    inheritance = scrapy.Field()
    prevalence = scrapy.Field()
    ageOfonset = scrapy.Field()
    ICD10 = scrapy.Field()
    OMIM = scrapy.Field()
    UMLS = scrapy.Field()
    MeSH = scrapy.Field()
    GARD = scrapy.Field()
    MedDRA = scrapy.Field()
    pubMed = scrapy.Field()
    url = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)


def filter_content(value):
    return value if len(value) > 0 else None


def filter_image_url(value):
    return "https:" + value if value[:2] == "//" else value


def publish_time_serializer(value):
    return int(
        time.mktime(datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timetuple())
    )


def publish_time_serializer(value):
    minutes_ago = re.compile(u".*?(\d+).*").search(value)
    hours_ago = re.compile(u".*?(\d+).*").search(value)
    days_ago = re.compile(u".*?(\d+).*").search(value)
    date = re.compile(u".*?(\d+)-(\d+).*").search(value)

    if minutes_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(
            minutes=int(minutes_ago.group(1))
        )
    elif hours_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(
            hours=int(hours_ago.group(1))
        )
    elif days_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(
            days=int(days_ago.group(1))
        )
    else:
        publish_time = datetime.datetime.today().replace(
            month=int(date.group(1)), day=int(date.group(2))
        )

    if publish_time is not None:
        return int(time.mktime(publish_time.timetuple()))
