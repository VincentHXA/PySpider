# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):
    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]
        return item


import MySQLdb
from twisted.enterprise import adbapi
class MySQLPipeline(object):
    def open_spider(self,spider):
        db = spider.settings.get('MYSQL_DB_NAME','scrapy_default')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')

        # MySQLdb
        # self.db_conn = MySQLdb.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        # self.db_cur = self.db_conn.cursor()

        # adbapi
        self.dbpool = adbapi.ConnectionPool('MySQLdb', host=host,
                                            db=db, user=user, passwd=passwd,
                                            charset='utf8')

    def close_spider(self, spider):
        # self.db_conn.commit()
        # self.db_conn.close()
        self.dbpool.close()

    def process_item(self, item, spider):
        # self.insert_db(item)
        self.dbpool.runInteraction(self.insert_db, item)
        return item

    def insert_db(self, tx, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )
        sql = 'INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s)'
        # self.db_cur.execute(sql, values)
        tx.execute(sql,values)

import redis
from scrapy import Item
class RedisPipeline:
    def open_spider(self,spider):
        host = spider.settings.get('REDIS_HOST', 'localhost')
        port = spider.settings.get('REDIS_PORT', 6379)
        index = spider.settings.get('REDIS_DB_INDEX', 0)
        passwd = spider.settings.get('REDIS_PASSWD', 'redis123')
        self.db_conn = redis.StrictRedis(host=host, port=port, db=index, password=passwd)
        self.item_i = 0

    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
       if isinstance(item, Item):
           item = dict(item)
           self.item_i += 1
           self.db_conn.hmset('book: %s' % self.item_i, item)

