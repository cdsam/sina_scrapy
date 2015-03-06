# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class TestscrapyItem(Item):
    level = Field()             #链接深度
    link = Field()              #链接
    parentLink = Field()        #父链接
    title= Field()              #链接名称
    
    

