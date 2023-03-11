from selenium import webdriver
from pyquery import PyQuery
from concurrent.futures import ThreadPoolExecutor
from os.path import exists
from os import mkdir

base_url = 'https://www.zmccx.com/57_57672/{}.html'

brower = webdriver.Chrome()
result = 'F:\\AjaxTest\\斗破苍穹\\斗破'


def save(title, c):
    mkdir(result) if not exists(result) else ''
    with open(f'{result}\\{title}.txt', 'w', encoding='utf-8') as f:
        f.write(c)


def r(page):
    try:
        print(base_url.format(page))
        brower.get(base_url.format(page))

        comment = brower.page_source
        pq = PyQuery(comment)
        c = pq('#content').text()
        title = pq('h1').text()
        print(title)
        # save(title, c)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # with ThreadPoolExecutor(50) as t:
    for i in range(21597158, 21599079 + 1):
        r(i)
        # t.submit(r, page=i)
    brower.close()
