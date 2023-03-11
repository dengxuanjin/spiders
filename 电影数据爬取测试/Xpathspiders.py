import requests

url = 'https://ssr1.scrape.center/page/1'

response = requests.get(url).text

from lxml import etree


xp = etree.HTML(response)

name = xp.xpath('//h2[@class="m-b-sm"]/text()')
categories = xp.xpath('//div[@class="categories"]//span/text()')
img = xp.xpath('//img[@class="cover"]/@src')
start_time = xp.xpath('//div[contains(@class, "m-v-sm")]/span/text()')
score = xp.xpath('//p[contains(@class, "score")]/text()')

print(score)