# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
	# define the fields for your item here like:
	title = scrapy.Field()
	brand = scrapy.Field()
	factory = scrapy.Field()
	serial = scrapy.Field()
	yearType = scrapy.Field()
	volumn = scrapy.Field()
	carStyle = scrapy.Field()
	guide_price = scrapy.Field()
	bare_price = scrapy.Field()
	buy_tax = scrapy.Field()
	deal_price = scrapy.Field()
	comn_ins = scrapy.Field()
	use_tax = scrapy.Field()
	trff_tax = scrapy.Field()
	license_fee = scrapy.Field()
	total_price = scrapy.Field()
	invoce_flg = scrapy.Field()
	promotion = scrapy.Field()
	deal_date = scrapy.Field()
	post_date = scrapy.Field()
	username = scrapy.Field()
	prov = scrapy.Field()
	city = scrapy.Field()
	sales_name = scrapy.Field()
	sales_telno = scrapy.Field()
	sales_addr = scrapy.Field()
	comment = scrapy.Field()
	curl_timestamp = scrapy.Field()
	url = scrapy.Field()
	data_id = scrapy.Field()
	pt = scrapy.Field()
