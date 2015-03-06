# -*- coding: utf-8 -*-

# Scrapy settings for testScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import MySQLdb

ITEM_PIPELINES = {    
    'testScrapy.pipelines.TestscrapyPipeline': 500,    
}  
 
DB_SERVER = 'MySQLdb'            # For detail, please see twisted doc
DB_CONNECT = {    
    'db': 'mysql',             # Your db   
    'user': 'dapp',              # 
    'passwd': 'dapp',            # 
    'host': '10.3.7.215',      # Your Server
    'charset': 'utf8',    
    'use_unicode': True,    
}   

BOT_NAME = 'testScrapy'

SPIDER_MODULES = ['testScrapy.spiders']
NEWSPIDER_MODULE = 'testScrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'testScrapy (+http://www.yourdomain.com)'
