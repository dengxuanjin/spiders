import requests

base_url = 'https://www.zhipin.com/wapi/zpgeek/recommend/job/list.json?degree=&scale=&stage=&salary=&payType=&multiBusinessDistrict=&page=2&sortType=1'
headers = {
    'authority': 'www.zhipin.com',
    'method': 'GET',
    'path': '/wapi/zpgeek/recommend/job/list.json?experience=&degree=&scale=&stage=&salary=&payType=&multiBusinessDistrict=&page=1&sortType=1',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '__g=Iemingzhan; __l=l=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3DIemingzhan&r=https%3A%2F%2Fntp.msn.cn%2F&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3DIemingzhan&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1672718084; gdxidpyhxdE=vUDLlAuXv2cipYt%2Bc1CQIt9bHKb6N2j%2F6kAe34QywYe9kUaJnlNIeaIZeZ1CpxW%2FWvJMD3dU%2F5gLiSuD8S%2FZOeACrgGDxNhHZiepRpDYG1j8aGPNLLwDTwRtaBCBi6ljfwZuZ3HmnKsDG1fiHupIQ2pZn2RAk6wIp3VWHr%2B%2B%2Fk%2BLrYbN%3A1672718994686; YD00951578218230%3AWM_NI=PeCdCI29IsgViNGlBBFad1tHeQoc7YcyRVd40XcoKoNsiWV%2FXFci4c8rqA5NiOMNux7RVcRWUa%2BH5cf3%2BZx4rBevaoev%2BwbW2FCUDybdgsmWssdy5ZziJ28Ybb9Ys%2BJma3g%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee93b866f8f08dd2e8678db48bb3c55f969e9ab0d153f2e7fe95c2548599abd2b12af0fea7c3b92a94bb8d85c243f2e78794e65eab92898dc14a86bfacd2f744a78fa184b653a1a79eb7e740f488ad90ca658eada7b8d5259c9aad8ab769fcaebfa2b846ab9183aff874f58e9a84d15d97bfe5a9b869a6ede5bbfb40b29eab97e465a7aae598e15df29a8db6c773a2bca994f05db1adac9ab852bab786d3bb53a2bef7baf2218ab3afd4e637e2a3; YD00951578218230%3AWM_TID=QnNBA0FSLHJFAFQBVRKAYnpzoHTSDOx2; wt2=Dd-stI6LVEzLNHLRV7tOeyS1rVh0-13A16hVN1XX71HHPucI91td2-ZuOeDAnFErhHDwgcrRYneKgBDFmL3h3kw~~; wbg=0; wd_guid=8010af71-c743-4377-b81e-9aa86b8dce45; historyState=state; _bl_uid=q8ljLcb2fq1p5e6yIwq4zh0ljUg0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1672718575; __zp_stoken__=6d98eZ158Lnx5fyN4IS0UcGwiQitQGT0EOyMoX2kiaA9CdwMxTEsbQWpgV1hlBR5HAnZ0YWoNBhgKSDAfbGUYRQ8cLg5jYnshcRMSUEl%2FDXIhETBcFWd1D0dKRzxOSysMQE9GABdsC282dD4%3D; __c=1672718083; __a=20465316.1672718083..1672718083.12.1.12.12; geek_zp_token=V1RN0lGeH82FtvVtRvyB8fKy6x7zvRxiU~',
    'referer': 'https://www.zhipin.com/web/geek/recommend?sortType=2',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': 'lhj92Nwu6vGtAq9f',
    'traceid': '32480825-6DCF-43A3-A409-3BC196726D89',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'x-requested-with': 'XMLHttpRequest',
    'zp_token': 'V1RN0lGeH82FtvVtRvyB8fKy-07jPWwy4~',
}
print(requests.post(base_url, headers=headers).text)