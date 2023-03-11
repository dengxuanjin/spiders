import requests
headers = {
    'Accept': "application/json, text/plain, */*",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkZ0tYbEZBbDBrS2gxb1owa0QzeTZBIiwic2lkIjoiNTU3MzI4NCIsImF1ZCI6IjEwMDAiLCJpc3MiOiJrYW9ndWppYS5jb20iLCJ0eXAiOiIxIiwibmJmIjoxNjcwNzY2NDM2LCJleHAiOjE2NzMzNTg0MzYsImlhdCI6MTY3MDc2NjQzNn0.HvhJX6TXtxxaX8mLhi84fTYAqhU5oQ2XD2fl7_k0_6g",
    'Content-Type': "application/json",
    'version_code': "3.1",
    'x-utm-source': "baidu",
    'x-utm-term': "56"
}
data = {
    'authority': 'service.kaogujia.com',
    'method': 'POST',
    'path': '/api/author/search?limit=50&page=1&sort_field=gmv&sort=0',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkZ0tYbEZBbDBrS2gxb1owa0QzeTZBIiwic2lkIjoiNTU3MzI4NCIsImF1ZCI6IjEwMDAiLCJpc3MiOiJrYW9ndWppYS5jb20iLCJ0eXAiOiIxIiwibmJmIjoxNjcwNzY2NDM2LCJleHAiOjE2NzMzNTg0MzYsImlhdCI6MTY3MDc2NjQzNn0.HvhJX6TXtxxaX8mLhi84fTYAqhU5oQ2XD2fl7_k0_6g',
    'content-length': '2',
    'content-type': 'application/json',
    'origin': 'https://www.kaogujia.com',
    'referer': 'https://www.kaogujia.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',

}

base_url = 'https://service.kaogujia.com/api/author/search?limit=50&page=1&sort_field=gmv&sort=0'
response = requests.post(base_url, data=data).text
print(response)