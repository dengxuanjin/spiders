import requests

headers = {
    'referer': 'https://huancang.art/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
}

import time
t = round(time.time()*1000)
Ji = "6RNRDpjjV6wZ2ssPxqeIBeSoV1ITXDdC"
e = "?flag=top&page=1&per_page=9&timestamp=" + str(t)
e = ("api/product/getproductsearch" + e + "&key=" + Ji).lower()
print(e)
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
with open("script.js", "r") as f:
    text = f.read()
ftx = execjs.compile(text)
headers['x-token'] = ftx.call("h", e)
# headers['signature'] = ftx.call("h", ftx.call("h", "7Tv7LrinK2bsNAi9TF2uui3ZIcoxK1WT"))
params = {
    'flag': 'top',
    'page': 1,
    'per_page': 9,
    'timestamp': t
}
base_url = f'https://api.onemeta.com.cn/api/product/getProductSearch'
response = requests.get(base_url, headers=headers, params=params).json()
print(response)
