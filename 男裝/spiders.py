'''
@Project   ：python2022
@File      ：京东男装.py
@IDE       ：PyCharm
@Author    ：DxJing
@Date      ：2023/3/10 19:28
@Objective :
'''

import requests

base_url = 'https://o2api.jd.com/data?body=%7B%22query%22%3A%22query%20getCommodities(%24ids%3A%20String)%7Bcommodities(ids%3A%20%24ids)%7BgroupId%2C%20groupName%2C%20productList%7BcanSell%20skuId%20name%20image%20title%20productImage%20commentCount%20goodRate%20currentPrice%20jdPrice%20pPrice%20pcpPrice%20plusPrice%20productExtInfo%20tag%20copyWriting%20copyWritingDown%20backUpWords%7D%7D%7D%22%2C%22operationName%22%3A%22getCommodities%22%2C%22variables%22%3A%7B%22ids%22%3A%22%5B19256279%2C19256324%2C19256301%2C19256303%2C19256194%5D%22%7D%2C%22previewTime%22%3A%22%22%2C%22config%22%3A%7B%22cache%22%3Afalse%2C%22trim%22%3Atrue%2C%22map%22%3A%7B%22keyBy%22%3A%22groupId%22%2C%22valueField%22%3A%22productList%22%7D%7D%7D&callback=o2e4dd0c94185ac79415153715c6cddc6e&_=1678499690205'

response = requests.get(base_url)
value = response.text[35:-2]

import json
print(json.loads(value))