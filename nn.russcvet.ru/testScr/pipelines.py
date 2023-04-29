# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy.crawler
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from openpyxl import Workbook

class TestscrPipeline:
    def __init__(self):
       self.work_book = Workbook()
       self.work_sheet = self.work_book.active
       self.work_sheet.append(['name', 'price'])

    def process_item(self, item, spider):
        self.work_sheet.append([item['name'], item['price']])

    def close_spider(self,spider):
        self.work_book.save('tbl.xls')