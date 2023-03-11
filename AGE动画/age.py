import requests
import json
import re

search_url = 'http://114.132.44.99:11334/ssszz.php?top=10&q={}'  # 搜索地址
base_url = 'http://agedmw.com/ssszz.php'  # 主页


# url = ''
# http://ss3.quelingfei.com:8080/wap.php?url=yj3456__v1437931824159489267127717988501231_7129326652592561183_hougong05ATX
# http://ss3.quelingfei.com:8080/wap.php?url=yj3456__v9449948336389396489527717988501231_7117542752803478564_hougong01ATX
def dowlaod(content):
    for i in content:
        print(i)


def detail(user):
    r = requests.get(base_url + user['url'])
    r.encoding = 'utf-8'
    text = re.findall('<li><a href="(.*?)">第(.*?)集</a></li>', r.text)
    for i in text:
        print(f'第{i[1]}集', end=' ')
    flag = input('\n输入(1.下载全部),(2.选择下载): ')
    if flag == '1':
        dowlaod(text)
    elif flag == '2':
        con = input('请输入需要选择的集数(使用空格隔开如 10 11 12):').split(' ')
        text = [ji for ji in text if ji[1] in con]
        dowlaod(text)
    else:
        print("选择有误")


def viduo(name):
    r = requests.get(search_url.format(name))
    if json.loads(r.content):
        user = None
        r.encoding = 'utf-8'
        print('当前搜索到的有:')
        content = json.loads(r.content)
        for i in content:
            print(i['title'])
        tc = input('请输入需要爬取哪一部电视:')
        for j in content:
            if j['title'] == tc:
                user = j
                break
        if user:
            detail(user)
        else:
            print('未查找到您输入的电视!，跳转回首页')
    else:
        print('无此类型电影')


if __name__ == '__main__':
    while True:
        name = input('请输入你需要搜索的番名(输入0结束查找):')
        if name != '0':
            viduo(name)
        else:
            break
