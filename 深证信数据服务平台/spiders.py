import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
import execjs
with open('js.js', 'r') as f:
    text = f.read()
    jst = execjs.compile(text)

mcode = jst.call('getResCode')
print(mcode)
headers = {
    'mcode': mcode,
    'Referer': 'https://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
}

data = {
    'scode': '000001-SZE',
    'sdate': '2022-02-04',
    'edate': '2023-02-04',
    'ctype': 0
}
response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008', headers=headers, data=data).json()
print(response)