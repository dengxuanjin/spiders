import time

import requests
base_url = 'https://api.bilibili.com/x/v2/reply/main?csrf=f3d49c308b231ffbb5ad927dab00849a&mode=3&next={' \
           '}&oid=381840324&plat=1&seek_rpid=&type=1'
# base_url = 'https://api.bilibili.com/x/v2/reply/main?csrf=c513ea685ec0451d1836b607b95684a7&mode=3&next={}&oid=504351640&plat=1&type=1'
header = {
    'content-type': 'application/json; charset=utf-8',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.52',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
# reply_url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=c513ea685ec0451d1836b607b95684a7&oid=431495381&pn={' \
#             '}&ps=10&root={}&type=1'
# reply_url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=c513ea685ec0451d1836b607b95684a7&oid=504351640&pn={}&ps=10&root={}&type=1'
reply_url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=f3d49c308b231ffbb5ad927dab00849a&oid=381840324&pn={' \
            '}&ps=10&root={}&type=1'

import pymysql

co = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='bibi', port=3306)
sa = co.cursor()


def save(data):
    with open('爱在西元前.csv', 'a+', encoding='utf-8') as f:
        f.write(data)


def savemysql(data):
    sa.execute('insert into detail(userid,mid,oid,username,sex,sign,message,categroy) values(%s,%s,%s,%s,%s,%s,%s,%s)',
               tuple(data))
    co.commit()
    print(data)


sum1 = 1
try:

    while True:
        if sum1 % 10 == 0:
            time.sleep(5)
        response = requests.get(base_url.format(sum1), headers=header).json()
        if response['data']['replies']:
            for i in response['data']['replies']:
                mid = str(i['mid'])
                save(
                    f"{i['rpid_str']},{mid},{str(i['oid'])},{i['member']['uname']},{i['member']['sex']},{i['member']['sign']},{str(i['content']['message'])},主评论\n")
                savemysql((i['rpid_str'], str(i['mid']), str(i['oid']), i['member']['uname'], i['member']['sex'],
                           i['member']['sign'], str(i['content']['message']), '主评论'))

                if i['count'] != 0:
                    rpid = i['rpid_str']
                    sum2 = 1
                    try:
                        while True:
                            if sum2 % 10 == 0:
                                time.sleep(5)
                            response2 = requests.get(reply_url.format(sum2, rpid), headers=header).json()
                            for x in response2['data']['replies']:
                                old = ''
                                try:
                                    old = [dt for dt in x['content']['at_name_to_mid'].values()][0]
                                except:
                                    old = mid
                                finally:
                                    save(
                                        f"{x['rpid_str']},{str(x['mid'])},{old},{x['member']['uname']},{x['member']['sex']},{x['member']['sign']},{str(x['content']['message'])},子评论\n")
                                    savemysql(
                                        (x['rpid_str'], str(x['mid']), str(old), x['member']['uname'], x['member']['sex'],
                                         x['member']['sign'], str(x['content']['message']), '子评论'))
                            sum2 += 1
                    except:
                        pass
        else:
            break

        print(f"第{sum1}页爬取成功")
        sum1 += 1
except Exception as e:
    print(e)
finally:
    co.close()
    print('爬取成功')
