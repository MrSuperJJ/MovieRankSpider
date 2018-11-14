# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute('scrapy crawl maoyan_spider -o movie_rank_spider/spiders/maoyan_movie_top100.json -s FEED_EXPORT_ENCODING=UTF-8'.split())