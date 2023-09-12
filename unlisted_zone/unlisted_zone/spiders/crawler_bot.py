import os
import sys
import scrapy
from ..items import UnlistedItem
sys.path.append(os.path.abspath('py_utils'))
from scraping_utils import ScrapingUtils as su
from common_utils import CommonUtils as cu


class UnlistedCrawler(scrapy.Spider):
    name = 'unlisted_bot'
    start_urls = {'https://unlistedzone.com/shares/'}
    df_path = '../datasets/unlisted_df'
    dict_path = '../datasets/unlisted_dict'
    columns = ['company', 'lot_size', 'last_price', 'cost_per_lot']

    company_path = "//*[@id='table-fill-1']/tbody/tr/td[1]/a/text()"
    lot_size_path = "//tbody[@class='table-hover']/tr/td[2]/text()"
    last_price_path = "//tbody[@class='table-hover']/tr/td[3]/text()"
    cost_per_lot_path = "//tbody[@class='table-hover']/tr/td[4]/text()"

    def parse(self, response, **kwargs):
        unlisted_item = UnlistedItem()
        unlisted_item['company'] = su.scrape_xpath(response, self.company_path)
        unlisted_item['lot_size'] = su.scrape_xpath(response, self.lot_size_path)
        unlisted_item['last_price'] = su.scrape_xpath(response, self.last_price_path)
        unlisted_item['cost_per_lot'] = su.scrape_xpath(response, self.cost_per_lot_path)

        value_list = [unlisted_item['company'], unlisted_item['lot_size'], unlisted_item['last_price'],
                      unlisted_item['cost_per_lot']]
        unlisted_dict = cu.create_dict(self.columns, value_list)
        cu.save_json(self.dict_path+'.json', unlisted_dict)
        unlisted_df = cu.create_df(unlisted_dict, self.columns)
        cu.save_df(unlisted_df, self.df_path, '.csv')
        cu.save_df(unlisted_df, self.df_path, '.xlsx')

        yield unlisted_item

