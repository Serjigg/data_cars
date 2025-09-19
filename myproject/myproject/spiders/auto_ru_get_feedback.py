import time

import scrapy
import csv
import os


class MySpider(scrapy.Spider):
    """ Собирает ссылки на отзывы """
    name = 'myspider'
    output_file = 'cars2.csv'

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['page', 'link_number', 'url', 'full_url'])

    def start_requests(self):
        for page in range(902, 9600):
            url = f'https://auto.ru/logbook/reviews/cars/?page={page}'
            time.sleep(0.25)
            yield scrapy.Request(url=url, callback=self.parse, meta={'page': page})

    def parse(self, response):
        page = response.meta['page']
        links = response.css('a.Link.LogbookListingSnippet__clicker-MqFUR::attr(href)').getall()

        with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for i, link in enumerate(links, 1):
                full_url = response.urljoin(link)
                writer.writerow([page, i, link, full_url])
                print(f"Сохранено: {full_url}")

        print(f"Страница {page}: сохранено {len(links)} ссылок")

        yield {
            'page': page,
            'links_count': len(links)
        }