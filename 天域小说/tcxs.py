from selenium import webdriver
from pyquery import PyQuery
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from concurrent.futures import ThreadPoolExecutor
from os.path import exists
from os import mkdir

base_url = 'https://www.zmccx.com/'
result = 'F:\\AjaxTest\\天域小说\\{}'
brower = webdriver.Chrome()
# def save(title, c):
#     mkdir(result) if not exists(result) else ''
#     with open(f'{result}\\{title}.txt', 'w', encoding='utf-8') as f:
#         f.write(c)


def r(search):
    try:
        print(base_url)

        brower.get(base_url)
        wait = WebDriverWait(brower, 10)
        title = wait.until(ec.title_contains('龙王传说_唐家三少新书_起点小说斗罗大陆3龙王传说在线阅读_天域小说网'))
        print(title)
        comment = brower.page_source

        print(comment)
        # pq = PyQuery(comment)
        # c = pq('#content').text()
        # title = pq('h1').text()
        # print(title)
        # save(title, c)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # with ThreadPoolExecutor(50) as t:
    # i = input("请输入需要需要搜索的小说:")
    r('')
    # t.submit(r, page=i)
    brower.close()
