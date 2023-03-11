import requests

url = 'https://ssr1.scrape.center/page/1'

response = requests.get(url).text

from bs4 import BeautifulSoup

bt = BeautifulSoup(response, 'lxml')

name = bt.find_all('h2', class_='m-b-sm')
img = bt.find_all('img', class_='cover')
categories = bt.find_all('div', class_='categories')
start_time = bt.find_all('div', class_=['m-v-sm', 'info'])
score = bt.find_all('p', class_='score')
print(score)
