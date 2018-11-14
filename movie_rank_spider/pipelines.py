# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter


class MovieRankSpiderPipeline(object):

    def process_item(self, item, spider):
        return item


class ItemCleanerPipeline(object):

    def process_item(self, item, spider):
        item.pop('score_integer')
        item.pop('score_fraction')
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('movie_rank_spider/spiders/maoyan_movie_top100.json', 'wb')
        self.exporter = JsonItemExporter(self.file, indent=4, encoding='utf8', ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()