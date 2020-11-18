# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from redis import Redis
from scrapy import signals, Spider
from scrapy.conf import settings
from scrapy.downloadermiddlewares.retry import RetryMiddleware

from genescrape import proxies


class GenescrapeAgentMiddleware(Spider):
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.settings.getlist("USER_AGENTS"))
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", random.choice(self.user_agents))

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class GenescrapeRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super(GenescrapeRetryMiddleware, self).__init__(settings)
        self.proxies = proxies.proxies

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.settings)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_exception(self, request, exception, spider):
        if len(self.proxies) > 0:
            request.meta["proxy"] = random.choice(self.proxies)
        return super(GenescrapeRetryMiddleware, self).process_exception(
            request, exception, spider
        )

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class GenescrapeProxyMiddleware(object):
    def __init__(self):
        redis_host = settings.get("REDIS_HOST")
        redis_port = settings.get("REDIS_PORT", default=6379)

        if redis_host is not None:
            self.r_client = Redis(host=redis_host, port=redis_port)

        self.proxies = proxies.proxies

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        if len(self.proxies) > 0:
            request.meta["proxy"] = random.choice(self.proxies)

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
