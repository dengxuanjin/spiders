import requests
from os import mkdir
from os.path import exists


def getimg(*kwargs):
    for i in kwargs[0]:
        dir = f"./img/{i['name']}{i['id']}"
        if not exists(dir):
            mkdir(dir)
            for img in range(len(i['img'])):
                response = requests.get(i['img'][img]).content
                with open(f'{dir}/{img}.jpg', 'wb') as f:
                    f.write(response)


import json


def writerjson(*args):
    for i in args[0]:
        json.dump(i, open(f"./detail/{i['name']}{i['id']}.json", 'w', encoding='utf-8'), ensure_ascii=False,
                  indent=2)


for j in range(1, 50):
    base_url = 'https://api5.hanfuhui.com/Trend/GetTrendListForHot?maxid=2754318&objecttype=album&count=10&page=%d'
    response = requests.get(base_url % j).json()
    title = [t['Content'] for t in response['Data']]
    name = [n['User']['NickName'] for n in response['Data']]
    fensicount = [n['User']['FansCount'] for n in response['Data']]
    Gender = [g['User']['Gender'] for g in response['Data']]
    ObjectId = [g['ID'] for g in response['Data']]
    img = []
    for i in response['Data']:
        list = []
        for i2 in i['Images']:
            list.append(i2['ImgSrc'] + '_700x.jpg')
        img.append(list)
    all = []
    for c in range(len(title)):
        data = {
            'title': title[c],
            'name': name[c],
            'fensicount': fensicount[c],
            'Gender': Gender[c],
            'img': img[c],
            'id': ObjectId[c]
        }
        all.append(data)
    getimg(all)
    writerjson(all)
    print(j)
    print(all)
# '_700x.jpg'
