import scrapy
from scrapy.loader import ItemLoader

class MovieItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_star = scrapy.Field()
    movie_releasetime = scrapy.Field()

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    start_urls = ['http://maoyan.com/board/4']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        movie_item_list = []
        for div in response.css('div.movie-item-info'):
            movie_name = div.css('p.name a::text').extract_first()
            movie_star = div.css('p.star::text').extract_first()
            movie_releasetime = div.css('p.releasstime::text').extract_first()
            movie_item = {
                'name': movie_name,
                'star': movie_star,
                'releasetime': movie_releasetime
            }
            movie_item_list.append(movie_item)
        self.log('movie_item_list: %s' % movie_item_list)

        item_loader = ItemLoader(item=MovieItem, response=response)
        item_loader





