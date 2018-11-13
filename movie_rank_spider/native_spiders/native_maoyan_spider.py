import requests
from lxml import etree
import pprint
from movie_rank_spider.parsers import maoyan_parser
import json

maoyan_url = 'http://maoyan.com/board/4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
movie_item_list = []
rank = 0

def parse_html(html_content):
    selector = etree.HTML(html_content)

    for dd in selector.xpath('''//dd'''):
        global rank
        movie_img_url = dd.xpath('''./a/img[@class='board-img']/@data-src''')[0]
        div = dd.xpath('''./div/div[@class='board-item-content']''')[0]
        movie_name = div.xpath('''./div/p[@class='name']/a/text()''')[0]
        movie_star = maoyan_parser.parse_movie_star(div.xpath('''./div/p[@class='star']/text()''')[0])
        movie_releasetime = maoyan_parser.parse_movie_releasetime(div.xpath('''./div/p[@class='releasetime']/text()''')[0])
        movie_score = maoyan_parser.parse_movie_score(div.xpath('''./div/p[@class='score']/i[@class='integer']/text()''')[0] + div.xpath('''./div/p[@class='score']/i[@class='fraction']/text()''')[0])
        rank += 1
        movie_item = {
            'rank': rank,
            'img_url': movie_img_url,
            'name': movie_name,
            'star': movie_star,
            'releasetime': movie_releasetime,
            'score': movie_score
        }
        movie_item_list.append(movie_item)

    next_page = selector.xpath('''//a[contains(text(), '下一页')]/@href''')
    if next_page:
        return movie_item_list, maoyan_url + next_page[0]
    return movie_item_list, None

url = maoyan_url
while url:
    html_content = requests.get(url, headers=headers).content.decode('utf-8')
    movie_item_list, url = parse_html(html_content)

if len(movie_item_list):
    with open('maoyan_movie_top100.json', 'w') as f:
        json.dump(movie_item_list, f, indent=4)


pprint.pprint(movie_item_list)