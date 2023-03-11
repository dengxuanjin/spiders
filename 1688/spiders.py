import requests
headers = {
    'authority': 's.1688.com',
    'method': 'GET',
    'path': '/company/pc/factory_search.htm?keywords=&spm=a26352.13672862.searchbox.input',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': '__wpkreporterwid_=0f3f24ae-4af9-4aa7-8f2e-67e9f94c60bc; cna=le7eG2EjsXkCAXcnIBTlNNTh; _m_h5_tk=b176a55e9f1a31ac05ad945944b6bfc9_1671204826984; _m_h5_tk_enc=e889f01e2300e8c85ad2a2eaacc3cc6b; xlly_s=1; cookie2=195507a99eb37cd1f0d3c8e1723e0df7; t=0e70392ee4b904ab34e9b6e1fe553199; _tb_token_=f35838e48e349; __cn_logon__=false; ali_ab=42.49.27.115.1671196214410.3; tfstk=ccDVBPX0iKp4NBn9J82ZaKoNE5hAZSagRTrUiFuTWDIFtuFciS7Tqt2L4lSPSSf..; l=fBQEIpWmT4IXdDxQBOfwPurza77ObIRAguPzaNbMi9fP_vCD5LchW6WpuCTkCnGVFsH6R3kbtBayBeYBqImOZzHoahInijHmnmOk-Wf..; isg=BIeH5YuhqILL1CwOJ78C55s0FjtRjFtu2T51h1l0vpY9yKeKYV2lvlSKboiWIDPm',
    'referer': 'https://s.1688.com/selloffer/offer_search.htm',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
}
response = requests.get('https://s.1688.com/company/pc/factory_search.htm?keywords=&spm=a26352.13672862.searchbox.input', headers=headers).text
print(response)