import requests
base_url = 'https://api.qimai.cn/rank/indexPlus/brand_id/2'
base_url2 = 'https://api.qimai.cn/rank/indexPlus/brand_id/1'
base_url3 = 'https://api.qimai.cn/rank/indexPlus/brand_id/0'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'qm_check=A1sdRUIQChtxen8tJ0NMMRcOUFseEHBeQF0NSjFNWCwycRd1QlhAXFECEUMgEQsfVkMBdAgBFE4SPVY7SFkKRmgHbwkcFHxSJlJVUVtWF1RaVVpbFgJDUk9UVElWBRsCEkQ%3D; gr_user_id=9e6acb3b-0cd2-45ca-9a52-9a8b64b48fdd; Hm_lvt_ff3eefaf44c797b33945945d0de0e370=1671799407,1672068311,1672106693,1672121284; PHPSESSID=ife307dkpc2099g69gkubh6ugi; ada35577182650f1_gr_session_id=5506c06f-5050-43f8-910b-fc9102aa579a; ada35577182650f1_gr_session_id_5506c06f-5050-43f8-910b-fc9102aa579a=true; Hm_lpvt_ff3eefaf44c797b33945945d0de0e370=1672121297; synct=1672121324.433; syncd=-1823',
    'origin': 'https://www.qimai.cn',
    'referer': 'https://www.qimai.cn/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
}

# 1页以后的params
params = {'page': '2', 'date': '2022-12-27', 'genre': '36', 'brand': 'all', 'country': 'cn', 'device': 'iphone'}
ps = ''
for i in params.values():
    ps += i
print(ps)
# 36allcniphone 第一页 第一页的params不能带page和date其他页都的带
# 22022-12-2736allcniphone 第二页
# 2022-12-27336allcniphone 第三页
# 2022-12-27364allcniphone 第四页
# 2022-12-27365allcniphone 第五页 后面的和第五页的一致

import time
t = round(time.time() * 1000)


import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
import execjs
with open('script.js', 'r') as f:
    text = f.read()
jst = execjs.compile(text)
analysis = jst.call("url", t, ps)
params['analysis'] = analysis
print(params)


response = requests.get(url=base_url, headers=headers, params=params)
print(response.json())