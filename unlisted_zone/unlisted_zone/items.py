# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnlistedItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    lot_size = scrapy.Field()
    last_price = scrapy.Field()
    cost_per_lot = scrapy.Field()
    pass
