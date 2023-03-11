import urllib

import requests
from urllib import request
from lxml import etree

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'uuid_n_v=v1; uuid=77FB3E00A9F111EDAA5BB1A1595AB3D2969CA7BDD942481D8A197F56259A3BF7; _lxsdk_cuid=1863fe1d66e52-04c3803c818621-7d5d547c-144000-1863fe1d66fc8; _lxsdk=77FB3E00A9F111EDAA5BB1A1595AB3D2969CA7BDD942481D8A197F56259A3BF7; _csrf=245e3d93d73e6c357e9dbde4772e71d2d2c877858cab73015da11d8b3c328bf8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1676296173,1676378510,1676388056,1676429249; __mta=150401929.1676109010862.1676388055788.1676429250859.25; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1676429492; _lxsdk_s=18652f84a19-1bb-20b-bc7%7C%7C13',
    'Host': 'www.maoyan.com',
    'Referer': 'https://www.maoyan.com/films/343521',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'timeStamp': 1676378518272,
    'index': 5,
    'signKey': '9f82deb03789b3566b78c055e73e61d4',
    'channelId': 40011,
    'sVersion': 1,
    'webdriver': 'false'
}


def getdata(url):
    response = requests.get(url, headers=headers, params=params)

    # response = request.urlopen(request.Request(url, headers=headers))
    # text = response.read().decode('utf-8')
    response.encoding = 'utf-8'
    text = response.text
    x = etree.HTML(text)
    print(text)
    with open('电影作者/content.txt', 'w', encoding='utf-8') as f1:
        with open('电影点赞/content.txt', 'w', encoding='utf-8') as f2:
            with open('电影评论/content.txt', 'w', encoding='utf-8') as f3:
                with open('电影发布时间/content.txt', 'w', encoding='utf-8') as f4:
                    with open('电影评分/fen.txt', 'w', encoding='utf-8') as f5:
                        with open('电影详情.csv', 'w', encoding='utf-8') as f6:
                            content = x.xpath('//div[@class="comment-content"]/text()')
                            start_time = x.xpath('//li//div[@class="time"]/@title')
                            name = x.xpath('//span[@class="name"]/text()')
                            good = x.xpath('//div[@class="approve "]/span[@class="num"]/text()')
                            fen = x.xpath('//ul[contains(@class,"score-star")]/@data-score')

                            for i in range(len(name)):
                                f1.write(name[i]+'\n')
                                f2.write(good[i]+'\n')
                                f3.write(content[i]+'\n')
                                f4.write(start_time[i]+'\n')
                                f5.write(fen[i]+'\n')
                                content[i] = content[i].replace("\n", '')
                                f6.write(f'{name[i]},{good[i]},{fen[i]},{start_time[i]},{content[i]}\n')
                                import pymysql
                                connect = pymysql.connect(user='root', password='123456', port=3306,host='127.0.0.1', database='maoyan')
                                cursor = connect.cursor()
                                print((name[i], good[i], fen[i], start_time[i], content[i]))
                                cursor.execute('insert into value values ("%s", "%s", "%s", %s, "%s")', (name[i], int(good[i]), content[i], start_time[i], int(fen[i])))

                                connect.commit()



if __name__ == '__main__':
    getdata('https://www.maoyan.com/ajax/films/1462626?timeStamp=1676465239911&index=1&signKey'
            '=9f82deb03789b3566b78c055e73e61d4&channelId=40011&sVersion=1&webdriver=false')
