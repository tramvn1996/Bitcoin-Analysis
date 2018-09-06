import scrapy
import json

from coinmap.items import CoinmapItem


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['https://coinmap.org/']
    start_urls = ['https://coinmap.org/api/v1/venues/']

    def parse(self, response):
        data = json.loads(response.body)

        for item in data.get('venues', []):
            element = CoinmapItem()

            element['name'] = item.get('name')
            element['venue_id'] = item.get('id')
            element['lattitude'] = item.get('lat')
            element['longitude'] = item.get('lon')
            element['category'] = item.get('category')
            element['created_on'] = item.get('created_on')

            yield element
