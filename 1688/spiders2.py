import requests
base_url = "https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/"
data2 = '{"cid":"FactorySearchPCConditionService:FactorySearchPCConditionService","methodName":"execute","params":"{\\"lv1RecCateSize\\":\\"50\\",\\"classifyByCategory\\":\\"true\\",\\"classifyByGeo\\":\\"true\\",\\"from\\":\\"pc_index_recommend\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}'

headers = {
    'cookie': 'cna=le7eG2EjsXkCAXcnIBTlNNTh; ali_ab=42.49.27.115.1671196214410.3; xlly_s=1; _m_h5_tk=96aa6d2a75cdb78169890450fa344cee_1671358776277; _m_h5_tk_enc=1e767508743f4a153957bfc06de23d4c; cookie2=113196f2960df6d9c98d9cd175899b9f; t=b559c6674a02a57a8f1aa0bb607e1144; _tb_token_=eba71868e377e; __cn_logon__=false; alicnweb=touch_tb_at%3D1671349060968; tfstk=cYbABvXrW820Tw2MzEEo7QpYTBDOatGvIj9tWw6vb8m3au3t5sfV-w3nsoOwLKFR.; isg=BC0t4JQGMhKYNtb8sflI1RVaPMmnimFch-Bvsm81QURb5k2YNtriLHv30LoA5nkU; l=fBQEIpWmT4IXd3RxBO5Bhurza779PBOb4sPzaNbMiIEGa6ZlQE40-NCFLJ9WYdtjgTCjueKrhWACFdLHR3fRwxDDBiNoQVI-cxvOGzHlR',
    'referer': 'https://sale.1688.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
}
# 通过扣js返回正确的sign的加密信息再去请求
import time
i = round(time.time()*1000)
with open("script.js", 'r') as f:
    text = f.read()
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

cjs = execjs.compile(text)
code = cjs.call("h", "96aa6d2a75cdb78169890450fa344cee" + "&" + str(i) + "&" + "12574478" + "&" + data2)
print(code)
# 5ed90c0631e92dcd57fbb397833c39d6
params = {'jsv': '2.6.1', 'appKey': '12574478', 't': i, 'sign': code, 'v': '1.0', 'type': 'jsonp', 'isSec': 0,
          'timeout': 20000, 'api': 'mtop.taobao.widgetService.getJsonComponent', 'dataType': 'jsonp',
          'jsonpIncPrefix': 'mboxfc', 'callback': 'mtopjsonpmboxfc9', 'data': data2}
# 注意data2的数据令牌cookie和taken不同时间段可能会有不同的变化
response = requests.get(url=base_url, headers=headers, params=params).text[18:-1]
import json

print(json.loads(response))