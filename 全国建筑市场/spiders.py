import requests
base_url = "https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg={}&pgsz=15&total=0"

headers ={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1670923861,1670937313; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1670937318',
    'Host': 'jzsc.mohurd.gov.cn',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'timeout': '30000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
}
for i in range(10):
    response = requests.get(url=base_url.format(i), headers=headers)
    response.encoding = response.apparent_encoding

    import subprocess
    from functools import partial
    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
    # 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
    import execjs

    with open('./js3.js', 'r', encoding='utf-8') as f:
        text = f.read()
    ctx = execjs.compile(text)
    data = ctx.call("h", response.text)
    print(data)
