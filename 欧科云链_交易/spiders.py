import time

import requests
# base_url = 'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict'
# headers = {
#     'Accept': 'application/json',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN',
#     'App-Type': 'web',
#     'Connection': 'keep-alive',
#     'Cookie': 'locale=zh_CN; first_ref=https%3A%2F%2Fcn.bing.com%2F; _okcoin_legal_currency=CNY; aliyungf_tc=6f6b363777bc54baad046cc705aead86af0bae0e1b688b9f0f1f83528374df90; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1671612886,1671615121,1671721790; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1671721926',
#     'devId': '0fc4ac25-b334-4f61-9237-90494f2fc11e',
#     'Host': 'www.oklink.com',
#     'Referer': 'https://www.oklink.com/zh-cn/btc/tx-list?limit=20&pageNum=1',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
#     'x-cdn': 'https://static.oklink.com',
#     'x-utc': '8',
# }
# import time
# t = round(time.time() * 1000)
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# # 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
# import execjs
# with open('script.js', 'r') as f:
#     text = f.read()
# jst = execjs.compile(text)
# x_apiKey = jst.call("getApiKey", t)
# headers['x-apiKey'] = x_apiKey
# params = {
#     't': t,
#     'limit': 20,
#     'offset': 20
# }

# 可以通过python的自带的base64库加base64的密
import base64
# bs = base64.b64encode('-b31e-4547-9299-b6d07b7631aba2c903cc|2782834793548600'.encode('utf-8'))
# print(bs)
# LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI3ODI4MzQ3OTM1NDg2MDA=
print(base64.b64encode(bytes(str(int(time.time()*100)))).decode(encoding='utf-8'))

# response = requests.get(url=base_url, headers=headers, params=params).json()
# print(response)