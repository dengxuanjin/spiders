import requests
# from lxml import etree
import re
import os

base_url = 'http://www.qiman59.com/'
url = 'http://www.qiman59.com/bookchapter/'

id = 16177
data = {
    'id': id,
    'id2': 1
}


def h(msg, dir):
    os.mkdir(dir)
    response3 = requests.get(msg).text
    content = re.findall("eval(.*)", response3)
    data = eval(content[0].split('}')[-2][:-15] + ")")

    import subprocess
    from functools import partial
    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
    # 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
    import execjs
    with open('script.js', 'r') as f:
        text = f.read()
    jst = execjs.compile(text)
    d1 = int(data[1])
    if d1 == 38:
        d1 -= 2
    elif d1 == 37:
        d1 -= 1
    d = jst.call('ge', data[0], d1, int(data[2]), data[3])
    d = eval(d[12:])
    sum = 1
    for i in d:
        response4 = requests.get(i).content
        save(response4, sum, dir)
        sum += 1
    print(f'{dir}爬取成功！')


def save(data, sum, dir):
    with open(f'{dir}/{sum}.jpg', 'wb') as f:
        f.write(data)


if __name__ == '__main__':

    response = requests.get(f"{base_url}/{id}/").text
    name = re.findall('<title>(.*?)</title>', response)[0].split('_')[0]
    os.mkdir(f"./{name}")
    r = re.findall('.*?<a href="(.*?)" class="ib">(.*?)</a>', response)
    [h(f"{base_url}{i[0]}", f"./{name}/{i[1]}") for i in r]
    response2 = requests.post(url, data=data).json()
    [h(f'{base_url}/{id}/{i["chapterid"]}.html', f"./{name}/{i['chaptername']}") for i in response2]
