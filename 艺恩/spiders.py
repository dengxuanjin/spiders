import requests
base_url = "https://www.endata.com.cn/API/GetData.ashx?year=2022&MethodName=BoxOffice_GetYearInfoData"

headers ={
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '46',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.endata.com.cn',
    'Origin': 'https://www.endata.com.cn',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    'X-Requested-With': 'XMLHttpRequest',}
data1 = {
    "year": 0,
    'MethodName': 'BoxOffice_GetYearInfoData'
}
for i in range(2008, 2023):
    data1['year'] = i
    response = requests.post(url=base_url, data=data1, headers=headers)
    response.encoding = response.apparent_encoding
    import subprocess
    from functools import partial
    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
    # 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
    import execjs

    with open('./scrpt.js', 'r', encoding='utf-8') as f:
        text = f.read()
    ctx = execjs.compile(text)
    data = ctx.call("webInstace.shell", response.text)
    print(data)
