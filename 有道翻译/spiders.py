'''
@Project   ：python2022
@File      ：有道翻译.py
@IDE       ：PyCharm
@Author    ：DxJing
@Date      ：2023/3/10 20:01
@Objective :
'''

import requests

base_url = 'http://fanyi.youdao.com/translate'




def getHtml(url, value):
    params = {
        "i": value,  # 待翻译的字符串
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16081210430989",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"

    }
    response = requests.post(url, data=params)
    response.encoding = 'utf-8'
    data = response.json()
    print(f'翻译为:{data["translateResult"][0][0]["tgt"]}')



if __name__ == '__main__':
    while True:
        value = input('请输入需要翻译的值(输入0结束):')
        if value != '0':
            getHtml(base_url, value)
        else:
            print('结束翻译!')
            break