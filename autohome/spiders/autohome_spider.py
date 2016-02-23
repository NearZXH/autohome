#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from autohome.items import AutohomeItem
import warnings
import time


# scrapy shell http://jiage.autohome.com.cn/price/carlist/p-13661
class AutohomeSpider(Spider):
	name = "autohome"
	allowed_domains = ["Autohome.com.cn"]
	start_urls = [
		"http://jiage.autohome.com.cn/price/carlist/p-13661"
	]

	def parse(self, response):
		sites = response.xpath("//div[@class='content']/div[@class='row']/div[@class='column grid-14 ']/div[@class='price-box']\
								/div[@class='price-box-bd']/ul/li")
		items = []
		i = 0
		for site in sites:
			item = AutohomeItem()
			name = site.xpath("div[@class='price-item-bd']/ul/li[@class='head-item']\
								/div[@class='txcon']/a/text()").extract()
			guide_price = site.xpath("div[@class='price-item-bd']/ul/li[3]/div[2]/text()").extract()
			bare_price = site.xpath("div[@class='price-item-bd']/ul/li[2]/div[2]/span/text()").extract()
			buy_tax = site.xpath("div[@class='price-item-bd']/ul/li[4]/div[2]/text()").extract()
			deal_price = 'asd'
			comn_ins = site.xpath("div[@class='price-item-bd']/ul/li[5]/div[2]/text()").extract()
			use_tax = site.xpath("div[@class='price-item-bd']/ul/li[8]/div[2]/text()").extract()
			trff_tax = site.xpath("div[@class='price-item-bd']/ul/li[9]/div[2]/text()").extract()
			license_fee = site.xpath("div[@class='price-item-bd']/ul/li[7]/div[2]/text()").extract()
			total_price = site.xpath("div[@class='price-item-bd']/ul/li[6]/div[2]/span/text()").extract()
			invoce_flg = '1'
			promotion = site.xpath("div[@class='price-item-bd']/ul/li[10]/div[2]/p/text()").extract()
			deal_date = site.xpath("div[@class='price-item-bd']/ul/li[11]/div[2]/text()").extract()[0]
			deal_date = deal_date[:4] + deal_date[5:7] + deal_date[8:10]
			post_date = site.xpath("div[@class='price-item-hd fn-clear']/div[@class='user-name']/span/text()").extract()[0]
			post_date = post_date[:4] + post_date[5:7] + post_date[8:10]
			username = site.xpath("div[@class='price-item-hd fn-clear']/div[@class='user-name']/\
									a[@class='uname']/text()").extract()
			prov = site.xpath("div[@class='price-item-bd']/ul/li[12]/div[2]/@pid").extract()
			city = site.xpath("div[@class='price-item-bd']/ul/li[12]/div[2]/@cid").extract()
			sales_name = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p[1]/a/text()").extract()
			if sales_name == []:
				sales_name = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p/text()").extract()
			sales_telno = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p[1]/\
									span/em[@class='phone-num']/text()").extract()
			if sales_telno == []:
				sales_telno = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p/text()").extract()
			sales_addr = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p[2]/span/text()").extract()
			if sales_addr == []:
				sales_addr = site.xpath("div[@class='price-item-bd']/ul/li[13]/div[2]/div/div/p/text()").extract()
			comment = site.xpath("div[@class='price-item-bd']/ul/li[14]/div[2]/p/text()").extract()
			curl_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			url = response.url
			data_id = url[-5:] + '-' + post_date
			pt = time.strftime('%Y%m%d', time.localtime(time.time()))

			name_list = name[0].encode('utf-8').split(' ')
			if len(name_list) == 5:
				item['brand'] = name_list[0]
				item['factory'] = ''
				item['serial'] = name_list[1]
				item['yearType'] = name_list[2]
				item['volumn'] = name_list[3]
				item['carStyle'] = name_list[4]
			elif len(name_list) == 6:
				item['brand'] = name_list[0]
				item['factory'] = name_list[1]
				item['serial'] = name_list[2]
				item['yearType'] = name_list[3]
				item['volumn'] = name_list[4]
				item['carStyle'] = name_list[5]
			else:
				warnings.warn('wrong values')
			item['guide_price'] = guide_price[0].encode('utf-8')
			item['bare_price'] = bare_price[0].encode('utf-8')
			item['buy_tax'] = buy_tax[0].encode('utf-8')
			item['deal_price'] = deal_price
			item['comn_ins'] = comn_ins[0].encode('utf-8')
			item['use_tax'] = use_tax[0].encode('utf-8')
			item['trff_tax'] = trff_tax[0].encode('utf-8')
			item['license_fee'] = license_fee[0].encode('utf-8')
			item['total_price'] = total_price[0].encode('utf-8')
			item['invoce_flg'] = invoce_flg
			item['promotion'] = promotion[0].encode('utf-8')
			item['deal_date'] = deal_date.encode('utf-8')
			item['post_date'] = post_date.encode('utf-8')
			item['username'] = username[0].encode('utf-8')
			item['prov'] = prov[0].encode('utf-8')
			item['city'] = city[0].encode('utf-8')
			item['sales_name'] = sales_name[0].encode('utf-8')
			item['sales_telno'] = sales_telno[0].encode('utf-8')
			item['sales_addr'] = sales_addr[0].encode('utf-8')
			item['comment'] = comment[0].encode('utf-8')
			item['curl_timestamp'] = curl_timestamp.encode('utf-8')
			item['url'] = url.encode('utf-8')
			item['data_id'] = data_id.encode('utf-8')
			item['pt'] = pt.encode('utf-8')

			items.append(item)
			output_str = items[i]['brand'] + '||' + items[i]['factory'] + '||' + items[i]['serial'] + '||' + \
						 items[i]['yearType'] + '||' + items[i]['volumn'] + '||' + items[i]['carStyle'] + '||' + \
						 items[i]['guide_price'] + '||' + items[i]['bare_price'] + '||' + items[i]['buy_tax'] + '||' + \
						 items[i]['deal_price'] + '||' + items[i]['comn_ins'] + '||' + items[i]['use_tax'] + '||' + \
						 items[i]['trff_tax'] + '||' + items[i]['license_fee'] + '||' + items[i]['total_price'] + '||' + \
						 items[i]['invoce_flg'] + '||' + items[i]['promotion'] + '||' + items[i]['deal_date'] + '||' +\
						 items[i]['post_date'] + '||' + items[i]['username'] + '||' + items[i]['prov'] + '||' + \
						 items[i]['city'] + '||' + items[i]['sales_name'] + '||' + items[i]['sales_telno'] + '||' + \
						 items[i]['sales_addr'] + '||' + items[i]['comment'] + '||' + items[i]['curl_timestamp'] + '||' + \
						 items[i]['url'] + '||' + items[i]['data_id']

			Filename = items[i]['data_id'] +'.txt'
			f = open(Filename, 'wb')
			f.write(output_str)
			f.close()
			i += 1
