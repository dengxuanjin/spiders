import requests

# base_url = 'https://api.bilibili.com/x/v2/reply/main?csrf=c513ea685ec0451d1836b607b95684a7&mode=3&next=' \
#            '{}&oid=388653711&plat=1&type=1'

import pymysql
base_url = 'https://api.bilibili.com/x/v2/reply/main?csrf=c513ea685ec0451d1836b607b95684a7&mode=3&next={' \
           '}&oid=431495381&plat=1&type=1'

# https://api.bilibili.com/x/v2/reply/main?csrf=c513ea685ec0451d1836b607b95684a7&mode=3&next=2&oid=388653711&plat=1&type=1\
def Getshengyudata(page, rpid='0'):
    url = ''
    if rpid != '0':
        url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=c513ea685ec0451d1836b607b95684a7&oid=388653711&pn={}&ps' \
              '=10&root=' + rpid + '&type=1'
        url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=c513ea685ec0451d1836b607b95684a7&oid=431495381&pn=1&ps=10&root=133225519440&type=1'
    else:
        url = base_url
    for i in requests.get(url.format(page)).json()['data']['replies']:
        with open('藏狐.csv', 'a+', encoding='utf-8') as f:
            f.write(
                f"{i['content']['message']}, {i['member']['uname']}, {i['member']['sex']}, {i['member']['sign']}\n")

            print(f"{i['content']['message']}, {i['member']['uname']}, {i['member']['sex']}, {i['member']['sign']}")
        print('剩余评论')


def GetData(page, rpid='0'):
    if rpid != '0':
        url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=c513ea685ec0451d1836b607b95684a7&oid=388653711&pn={}&ps' \
              '=10&root=' + rpid + '&type=1'
        print('子评论')
    else:
        url = base_url
    for i in range(0, page):
        print(f"第{i + 1}列爬取成功")
        response = requests.get(url.format(i)).json()
        for i in response['data']['replies']:
            with open('藏狐.csv', 'a+', encoding='utf-8') as f:
                f.write(
                    f"{i['content']['message']}, {i['member']['uname']}, {i['member']['sex']}, {i['member']['sign']}\n")
                print(f"{i['content']['message']}, {i['member']['uname']}, {i['member']['sex']}, {i['member']['sign']}")
            count = i['count']
            rpid = i['rpid_str']
            if count != 0:
                allpage = count // 10
                if count % 10 == 0:
                    GetData(allpage, rpid)
                else:
                    GetData(allpage, rpid)
                    Getshengyudata(allpage)


response = requests.get(base_url.format(0)).json()
all_count = response['data']['cursor']['all_count']
allpage = all_count % 20
if allpage == 0:
    GetData(allpage // 20)
else:
    GetData(all_count // 20)
    # Getshengyudata(allpage)
