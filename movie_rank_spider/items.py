# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from movie_rank_spider.parsers import maoyan_parser


class MovieRankSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    rank = scrapy.Field()
    img_url = scrapy.Field()
    name = scrapy.Field()
    star = scrapy.Field(
        input_processor = MapCompose(maoyan_parser.parse_movie_star),
        output_processor = MapCompose()
    )
    releasetime = scrapy.Field(
        input_processor = MapCompose(maoyan_parser.parse_movie_releasetime)
    )
    score_integer = scrapy.Field()
    score_fraction = scrapy.Field()
    score = scrapy.Field(
        input_processor = MapCompose(maoyan_parser.parse_movie_score)
    )