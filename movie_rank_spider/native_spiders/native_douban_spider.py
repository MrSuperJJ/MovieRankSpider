import requests
from lxml import etree

douban_url = 'http://movie.douban.com/top250'
movie_name_list = []

def parse_html(html_content):
    selector = etree.HTML(html_content)
    for movie_item in selector.xpath('''//ol[@class='grid_view']/li'''):
        movie_name = movie_item.xpath('''div//span[@class='title']/text()''')
        movie_name_list.append(movie_name)

    print(len(movie_name_list))
    # next_page = selector.xpath('''//span[@class='next']/a/@href''')
    # if next_page:
    #     return movie_name_list, douban_url + next_page[0]
    return movie_name_list, None

url = douban_url
while url:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    html_content = requests.get(douban_url, headers=headers).content.decode('utf-8')
    movies, url = parse_html(html_content)
