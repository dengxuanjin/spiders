import time
import requests

base_url = 'https://api.bilibili.com/x/v2/reply/main?csrf=ad39b850cdc15c822e212ef405690688&mode=3&next={' \
           '}&oid=381840324&plat=1&type=1'
reply_url = 'https://api.bilibili.com/x/v2/reply/reply?csrf=ad39b850cdc15c822e212ef405690688&oid=381840324&pn={' \
            '}&ps=10&root={}&type=1'


def save(data):
    with open('爱在西元前.csv', 'a+', encoding='utf-8') as f:
        f.write(data)


import pymysql

con = pymysql.connect(user='root', password='123456', port=3306, database='bibi', host='127.0.0.1')

py = con.cursor()


def savemysql(data):
    py.execute('insert into detail(userid,mid,oid,username,sex,sign,message,categroy) values(%s,%s,%s,%s,%s,%s,%s,%s)',
               tuple(data))
    con.commit()
    print(data)


sum1 = 1
try:

    while True:
        if sum1 % 20 == 0:
            time.sleep(5)
        response1 = requests.get(base_url.format(sum1)).json()
        for i in response1['data']['replies']:
            mid = str(i['mid'])
            save(
                f"{i['rpid_str']},{mid},{str(i['oid'])},{i['member']['uname']},{i['member']['sex']},{i['member']['sign']},{str(i['content']['message'])},主评论\n")
            savemysql((i['rpid_str'], str(i['mid']), str(i['oid']), i['member']['uname'], i['member']['sex'],
                       i['member']['sign'], str(i['content']['message']), '主评论'))
            if i['count'] != 0:
                sum2 = 1
                try:
                    while True:
                        if sum2 % 15 == 0:
                            time.sleep(5)
                        response2 = requests.get(reply_url.format(sum2, i['rpid_str'])).json()
                        for x in response2['data']['replies']:
                            oid = ''
                            try:
                                oid = [dt for dt in x['content']['at_name_to_mid'].values()][0]
                            except:
                                oid = mid
                            finally:
                                save(
                                    f"{x['rpid_str']},{str(x['mid'])},{oid},{x['member']['uname']},{x['member']['sex']},{x['member']['sign']},{str(x['content']['message'])},子评论\n")
                                savemysql(
                                    (x['rpid_str'], str(x['mid']), str(oid), x['member']['uname'], x['member']['sex'],
                                     x['member']['sign'], str(x['content']['message']), '子评论'))
                        sum2 += 1
                except:
                    pass
        print(f'第{sum1}页爬取成功')
        sum1 += 1
except Exception as e:
    print(e)
finally:
    con.close()
    py.close()
    print('爬取成功')


