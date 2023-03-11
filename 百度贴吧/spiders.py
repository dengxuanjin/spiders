'''
@Project   ：python2022
@File      ：百度贴吧图片.py
@IDE       ：PyCharm
@Author    ：DxJing
@Date      ：2023/3/10 19:28
@Objective :
'''
import requests

base_url = 'https://tieba.baidu.com/p/2460150866?red_tag=3274567537'
page_url = 'https://tieba.baidu.com/p/2460150866?pn={}&ajax=1&t=1678442341243'


def getHtml(url):
    response = requests.get(url)
    response.encoding = 'utf-8'

    from lxml import etree
    html = etree.HTML(response.text)
    img = html.xpath('//img[@class="BDE_Image"]/@src')
    saveimg(img)
    for i in range(2, 11):
        response2 = requests.get(page_url.format(i))
        response.encoding = 'utf-8'
        html = etree.HTML(response2.text)
        img2 = html.xpath('//img[@class="BDE_Image"]/@src')
        saveimg(img2)
    pass


page = 1


def saveimg(img):
    global page
    j = 1
    import os
    if not os.path.exists(f'./img/第{page}页'):
        os.mkdir(f'./img/第{page}页')
    for i in img:
        response = requests.get(i).content
        with open(f'./img/第{page}页/{j}.png', 'wb+') as f:
            f.write(response)
        j += 1
    print(f'第{page}页爬取成功!')
    page += 1


if __name__ == '__main__':
    import os
    if not os.path.exists('./img'):
        os.mkdir(f'./img')
    getHtml(base_url)
