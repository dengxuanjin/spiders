import requests
from bs4 import BeautifulSoup as bs
import pymysql
# from multiprocessing.dummy import Pool
from concurrent.futures import ThreadPoolExecutor

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, database='spiders.py')
data = []
cursor = db.cursor()
n = 0


# # try: cursor.executemany('insert into book(name, url, img, author, introduce) values (%s, %s, %s, %s, %s)',
# [('dsdg', '1111', 'img[j]', 'author[j]', 'introduce[j]')]) print('susccse') cursor.commit() # except: #     print(
# 'shibai') #     db.rollback() db.close()

def getdata(page):
    # print(page)
    cursor = db.cursor()
    from lxml import etree
    base_url = 'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_%d.html' % page
    response = requests.get(base_url)
    response.encoding = 'utf-8'
    response = response.text
    etree = etree.HTML(response)
    url = etree.xpath('//div[@class="alltable"]//dl/dt/a/@href')
    img = etree.xpath('//div[@class="alltable"]//dl/dt/a/img/@src')
    name = etree.xpath('//div[@class="alltable"]//dl/dd//li/strong/a/text()')
    author = etree.xpath('//div[@class="alltable"]//dl/dd//li[@class="zz"]/a/text()')
    introduce = etree.xpath('//div[@class="alltable"]//dl/dd//li/p/a/text()')
    print(name)
    j = 0
    urls = []
    for i in url:
        urls.append("https://" + i.split('//')[1])
        global n
        n += 1
    if len(introduce) == 30:

        for j in range(0, 30):
            data.append({
                "name": name[j],
                'url': urls[j],
                'img': img[j],
                'author': author[j],
                "introduce": introduce[j]
            })

            # print(name[j])
            # 60、309
            cursor.execute('insert into book(name, url, img, author, introduce) values (%s, %s, %s, %s, %s)',
                           (name[j], urls[j], img[j], author[j], introduce[j]))
            db.commit()
    else:
        print(page)


# with ThreadPoolExecutor(30) as t:
# for page in range(1, 335):
# t.submit(getdata, page=page)
for page in range(1, 335):
    getdata(page)
# pool = Pool(30)
# for i in range(1, 10):
#     pool.map(getdata, i)
# print(data)
print(n)
