import requests


base_url = 'https://cn.bing.com/search?q=%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9'

headers = {
    'authority': 'cn.bing.com',
    'method': 'GET',
    'path': '/search?q=%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_EDGE_V=1; MUID=00C6E638B96B652F0037F470B8286403; MUIDB=00C6E638B96B652F0037F470B8286403; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=E20E43F2E8A64EB4BDAC1B4EF28BAFEF&dmnchg=1; USRLOC=HS=1; ANON=A=65D10CF53FA75B35755C9209FFFFFFFF&E=1b8f&W=1; PPLState=1; KievRPSSecAuth=FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACMfgBjmdGkReCASBQFVqZCN0VoxxIhj751b5SfkZ4biP6XLDDbv5kfP/6TomZt6UaFQhcIVLvmjo/etWUgF+qbB2ga8gVRXOQid8na1HvneKGgVxB+haM68UfeiDeyuEg+UV8s3SdlE/a9lJnhD4eix7gn0YjLhVMqI5UqrveV3a3qgaxJDnqZ+HA7iHm4cWt7dhbQFV43JUuUs9e6FYC2QzCFvq53ko9TVwXUC8Z++IGO/ky3qITvMZEDcdJ1wRQuIXafGA31cUjwo5JCj37XFD5PtbCDPTUEmPCx6/pr4ilgsn9FNFS1vqyeRjD1GgYm5nPTItwDryUquz43pDtNirc6lpTvj3P/Hw9QQDwILZd9QoaGUC39IuUPMy2Gm+WylY1LNcuohQrFbHhbvp7By+80ZDm7Cn5334wk5Kh/Uwb5gWTesnzxhy/TE9H82YuGgfbxDgiwCBumZ74QxafE619JTAvE85dWAwq5zLADg5V0zz9oRkintHeIf33Y9uk+6PviETX31/4TTtqar493RF77YoUl81JGok4mCL+TidY10kVN6MrPx3S2heoaxjaD9w4n1xV8ePoZ+LUbFCwRVhQ9xM4Gou85mB0x1oDmdwOgdJQj6F3jxQmwy0rzjjBDLhD52QUPVesOtQoT3m1UTbbCjSpJkdVMJrZJNK/eJZvhN7FsiUCU7eiz7GFz26+y3EGoIHKQJ4BL/hvkWwK6xtPOuyK638Fq2ddhbm8aXs1KQ/pFtUuvrxona0VcWQQ6y/Z64IOS5JX6zGCx00I+OI7ztiR8FM6EDxGtYSwRSKKAYPvaMYy88aHmpnFMTkfg2ViRli/IGZawsyxkgzCFKeuZq4yf0uUvx63dcmDDgcWF1tboBymJ0q6RNqrVE/FOtyrPaoAdf96MbywsSWgJ7Bnt65TpndaW1C77f/3tC7lrRdE9lHRMZmtTx36VM4/BNVDDNx1QIp58DqdSKwg0BF+tS0hgeMj1LGBi1VyR906F2GDz0lVFQJSwhAppQ7XUjx1yXYktkX6smbkfNA4gMAcDcPd8Ya/pNJVLXKzoMDV6mQji1XpgzwJVP6ZK1KVI1ZNcoipg3hQm89fD9BoBtTLCh+7P0OBTiuLTcKM5QNv1YLqKtDNAqG88naN7RL4/3GdlYfJbX0z0wE6PRSEnZB+n3A1ETF2NeTQ5U1fMuhbIJamoE9028ZCVrXAupLPEsYWRrpV7mbIjyqs68r9V9mpReioCxfFpmvOmvKwyIJ8T/7fYBTi/h/yFwW+PaxSUSX8i432FBD94n5ZTUX4DFVsosjVAPqu2WKVnIowLoMx8IyjhFIWFqFdafh27TjczEenAC1bl0BsRTE6wVf6A+u6OZf9Px7P2ftCffqxGA8Q3cUAH81xxMzvTrvJQvf7Dr6259AmGZ1; MMCASM=ID=E1C0EEAEA483447AB341108E53D425A5; TTRSL=en; _UR=QS=0&TQS=0; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMS0xMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NiwiSHNjIjpmYWxzZX0=; imgv=lodlg=1&gts=20230130; ZHCHATSTRONGATTRACT=TRUE; ANIMIA=FRE=1; ABDEF=V=13&ABDV=11&MRNB=1675687124906&MRB=0; SUID=A; _EDGE_S=SID=3713CF3B534B6A452B91DD8A52996B93; WLS=C=9e8bb5737fdbb2ca&N=dg; SRCHUSR=DOB=20221025&T=1675756480000; _SS=SID=3713CF3B534B6A452B91DD8A52996B93&R=200&RB=0&GB=0&RG=200&RP=200; _TTSS_IN=hist=WyJlbiIsInpoLUhhbnMiLCJhdXRvLWRldGVjdCJd; ipv6=hit=1675760086865&t=4; _tarLang=default=ja; _TTSS_OUT=hist=WyJ6aC1IYW5zIiwiZW4iLCJqYSJd; _RwBf=ilt=419&ihpd=0&ispd=1&rc=200&rb=0&gb=0&rg=200&pc=200&mtu=0&rbb=0&g=0&cid=&clo=0&v=1&l=2023-02-07T08:00:00.0000000Z&lft=2023-01-18T00:00:00.0000000-08:00&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2023-02-07T08:46:12.4528275+00:00&rwred=0&wls=&lka=0&lkt=0&TH=; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&BZA=0&BRW=XW&BRH=M&CW=1536&CH=754&SCW=1519&SCH=2727&DPR=1.3&UTC=480&DM=0&EXLTT=31&HV=1675759574&PRVCW=1536&PRVCH=754&PR=1.25&VCW=1519&VCH=754; SNRHOP=I=&TS=; _U=1TAihPRYRwC7klogJYlqEUfiUQeU_IQfw2t2SQjN1qiiazEmh48Ee2YhIVtvwoUar-ZDQBfmsbnp0fQ1PH6cqfEgsgjGVD3SvHUoAJCx8iV11r22kgrQvJgHhJxOjak3gxXuoe6AlV-qGpUbl7RCli0lkCQ08H5JIh2ak_9sbinK-K5bc-9aDNczmQlWC7EIi',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"109.0.1518.78"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Microsoft Edge";v="109.0.1518.78", "Chromium";v="109.0.5414.120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
    'x-edge-shopping-flag': '1',
}
response = requests.get(url=base_url, headers=headers, params={'q': '哔哩哔哩'})
response.encoding = 'utf-8'
print(response.text)