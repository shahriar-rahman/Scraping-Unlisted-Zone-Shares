# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import os
import sys
sys.path.append(os.path.abspath('py_utils/'))
from sqlite_utils import SqliteUtils as sql_utils


class UnlistedZonePipeline:
    def __init__(self):
        path_db = '../database/db_unlisted.db'
        self.connect = self.sqlite3_connection(path_db)
        self.cursor = self.sqlite3_cursor(self.connect)
        self.create_table()

    @staticmethod
    def sqlite3_connection(path_db):
        return sql_utils.create_connection(path_db)

    @staticmethod
    def sqlite3_cursor(connection):
        return sql_utils.create_cursor(connection)

    def create_table(self):
        self.cursor.execute('''create table if not exists 
                            unlisted_shares(company text, lot_size text, last_price text, cost_per_lot text)
                            ''')

    def process_item(self, item, spider):
        print("Pipeline: ", item)
        self.store_db(item)
        return item

    def store_db(self, item):
        for index in range(len(item['company'])):
            self.cursor.execute('''insert into unlisted_shares values (?, ?, ?, ?)''',
                                (item['company'][index],  item['lot_size'][index],
                                 item['last_price'][index], item['cost_per_lot'][index])
                                )
        self.connect.commit()
        self.connect.close()
