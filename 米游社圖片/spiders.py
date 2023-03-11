import requests
import csv
base_url = f'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=29&gids=2&is_good=false&last_id=%s&is_hot' \
           f'=false&page_size=20&sort_type=2'
last_id = ''
while True:
    response = requests.get(base_url % last_id).json()
    img = [ig['post']['cover'] for ig in response['data']['list']]
    last_id = response['data']['last_id']
    name = [n['post']['subject'] for n in response['data']['list']]
    z = [x for x in zip(name, img)]
    for data in z:
        flag = 1
        try:
            with open('E:\\python項目\\AjaxTest\\米游社圖片\\img2\\' + data[0] + '.png', 'wb') as f:
                print('E:\\python項目\\AjaxTest\\米游社圖片\\img2\\' + data[0] + '.png')
                ig = requests.get(data[1]).content
                f.write(ig)
        except Exception as e:
            flag = 0
            print(data[0])
        finally:
            with open('detail.csv', 'a+', encoding='utf-8') as f:
                wr = csv.writer(f)
                wr.writerow([data[0], data[1], flag])