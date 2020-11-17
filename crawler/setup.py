# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='genescrape',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = genescrape.settings']},
    install_requires=['scrapy', 'elasticsearch', 'redis']
)
