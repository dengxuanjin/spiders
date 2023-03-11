from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
import requests
import pymysql

detail_url = 'https://www.17k.com/ck/group/thread?type=0&page=%d&num=20&bookId=%s&appKey=2406394919'
# import http.client
# http.client.HTTPConnection._http_vsn = 10
# http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, database='spiders.py')
cuser = db.cursor()
import asyncio


def getdetail(dir):
    count = 0
    value = dir[1].split('book/')[1].replace('.html', '')
    frist_url = detail_url % (1, value)
    number = requests.get(frist_url).json()['totalNum']
    data = []
    for j in range(1, number // 20 + 1):
        url = detail_url % (j, value)
        response = requests.get(url).json()
        for i in range(20):
            data.append({
                'username': response['data'][i]['userInfo']['nickname'],
                'bookname': dir[0],
                'content': response['data'][i]['summary'],
                'bookid': dir[2],
                'icon': response['data'][i]['userInfo']['avatarUrl'],
                'create_time': str(datetime.fromtimestamp(response['data'][i]['createTime'] // 1000))

            })
            count += 1
    if number != 0:
        if number > 20:
            j = number // 20 + 1
            url = detail_url % (j, value)
            response = requests.get(url).json()
            for i in range(number % 20):
                data.append({
                    'username': response['data'][i]['userInfo']['nickname'],
                    'bookname': dir[0],
                    'content': response['data'][i]['summary'],
                    'bookid': dir[2],
                    'icon': response['data'][i]['userInfo']['avatarUrl'],
                    'create_time': str(datetime.fromtimestamp(response['data'][i]['createTime']//1000))
                })
                count += 1
        else:
            url = detail_url % (1, value)
            response = requests.get(url).json()
            for j in range(number):
                data.append({
                    'username': response['data'][j]['userInfo']['nickname'],
                    'bookname': dir[0],
                    'content': response['data'][j]['summary'],
                    'bookid': dir[2],
                    'icon': response['data'][j]['userInfo']['avatarUrl'],
                    'create_time': str(datetime.fromtimestamp(response['data'][j]['createTime'] // 1000))
                })
                count += 1
        for i in data:
            cuser.execute("insert into detail(username,bookname,content,bookid,icon,create_time) values(%s,%s,%s,%s,%s,%s)", tuple(i.values()))
            db.commit()
        print(count)
    else:
        cuser.execute('insert into detail(username,bookname,content,bookid,icon,create_time) values(%s,%s,%s,%s,%s,%s)',
                      ('', dir[0], '无评论', dir[2], '无', '无'))
        db.commit()
        print("无评论")


cuser.execute('select name,url,id from book')
book = cuser.fetchall()
# from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(2) as t:
    for i in book:
        t.submit(getdetail, dir=i)
    # asyncio.run(getdetail(i))

cuser.close()
db.close()
