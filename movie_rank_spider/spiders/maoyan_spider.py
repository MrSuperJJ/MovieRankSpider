import scrapy
from scrapy.loader import ItemLoader
from movie_rank_spider.parsers import maoyan_parser

class MovieItem(scrapy.Item):
    rank = scrapy.Field()
    img_url = scrapy.Field()
    name = scrapy.Field()
    star = scrapy.Field()
    releasetime = scrapy.Field()
    score = scrapy.Field()

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    start_urls = ['http://maoyan.com/board/4']
    rank = 0

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        for dd in response.css('dd'):
            self.rank += 1
            div = dd.css('''div div.board-item-content''')
            item = MovieItem()
            item['rank'] = self.rank
            item['img_url'] = dd.css('''a img.board-img::attr(data-src)''').extract_first()
            item['name'] = div.css('div p.name a::text').extract_first()
            item['star'] = maoyan_parser.parse_movie_star(div.css('div p.star::text').extract_first())
            item['releasetime'] = maoyan_parser.parse_movie_releasetime(div.css('div p.releasetime::text').extract_first())
            item['score'] = maoyan_parser.parse_movie_score(
                div.css('''div p.score i.integer::text''').extract_first() +
                div.css('''div p.score i.fraction::text''').extract_first())
            yield item

        next_page = response.xpath('''//a[contains(text(), '下一页')]/@href''')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)
        else:
            pass






