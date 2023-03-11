import requests
from lxml import etree


# https://book.qidian.com/info/1036170277/
# https://read.qidian.com/chapter/NjAhWJLJfQTlwGcoSQesFQ2/OVY32klgGX9Ms5iq0oQwLQ2/
base_url = 'https://vipreader.qidian.com/chapter/1036170277/745447291/'

headers1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_yep_uuid=d78fc724-3744-c26c-ae88-5790b16c81e3; e1=%7B%22pid%22%3A%22qd_P_vipread%22%2C%22eid%22%3A%22qd_R35%22%2C%22l2%22%3A6%2C%22l1%22%3A40%7D; e2=%7B%22pid%22%3A%22qd_P_vipread%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1668496417_953097764; _csrfToken=unCvAP6qNtWJma6RyCUCAMyrR650ywZ7JOzZY1Ij; fu=2014973649; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; _ga_D20NXNVDG2=GS1.1.1669708331.2.1.1669708356.0.0.0; _ga_VMQL7235X0=GS1.1.1669708330.2.1.1669708356.0.0.0; traffic_utm_referer=https%3A//cn.bing.com/; Hm_lvt_f00f67093ce2f38f215010b699629083=1678291810; _gid=GA1.2.1450550991.1678291811; ywopenid=0F2F30FC35A1D2E1D88E21F7565D8D14; rcr=1036170277%2C1031777108%2C1031940621; bc=1036170277; ywguid=487127026; ywkey=yw1xddX1RWvR; ywGameUserId=23782927045694700; pageOps=1; lrbc=1036170277%7C745421524%7C1; _gat_gtag_UA_199934072_2=1; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A117%22%2C%22l2%22%3A1%2C%22l1%22%3A11%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%2C%22l1%22%3A11%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1678293464; _ga=GA1.2.1383719396.1668496419; _ga_FZMMH98S83=GS1.1.1678291810.8.1.1678293465.0.0.0; _ga_PFYW0QLV3P=GS1.1.1678291810.8.1.1678293465.0.0.0",
    "Host": "vipreader.qidian.com",
    "Referer": "https://book.qidian.com/",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
}



headers2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "_yep_uuid=a65ee1cf-41c1-0802-f4ea-3c7b4b85c554; e1=%7B%22pid%22%3A%22qd_P_vipread%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_P_vipread%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; newstatisticUUID=1668496417_953097764; _csrfToken=unCvAP6qNtWJma6RyCUCAMyrR650ywZ7JOzZY1Ij; fu=2014973649; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; _ga_D20NXNVDG2=GS1.1.1669708331.2.1.1669708356.0.0.0; _ga_VMQL7235X0=GS1.1.1669708330.2.1.1669708356.0.0.0; traffic_utm_referer=https%3A//cn.bing.com/; _gid=GA1.2.1450550991.1678291811; rcr=1036170277%2C1031777108%2C1031940621; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A117%22%2C%22l2%22%3A1%2C%22l1%22%3A11%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%2C%22l1%22%3A11%7D; Hm_lvt_f00f67093ce2f38f215010b699629083=1678291810,1678356955; navWelfareTime=1678356955719; ywguid=487127026; ywkey=ywSj1jUu14tQ; ywopenid=0F2F30FC35A1D2E1D88E21F7565D8D14; lrbc=1036170277%7C745447291%7C1; bc=1036170277; _ga=GA1.1.1383719396.1668496419; Hm_lpvt_f00f67093ce2f38f215010b699629083=1678361015; _ga_FZMMH98S83=GS1.1.1678361009.10.1.1678361051.0.0.0; _ga_PFYW0QLV3P=GS1.1.1678361009.10.1.1678361051.0.0.0",
    "Host": "vipreader.qidian.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
}




def getdata(url):
    # while True:
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         response = response.text
    #         break
    #     print(f'当前获取状态为{response.status_code},继续请求中。')
    #
    # eml = etree.HTML(response)
    # name = eml.xpath('//h2[@class="book_name"]/a/text()')
    # search_url = eml.xpath('//h2[@class="book_name"]/a/@href')
    # print(name)
    # print(['https:'+i for i in search_url])
    response = requests.get(url, headers=headers2).text

    print(response)
    # eml = etree.HTML(response)

    # content = eml.xpath('//div[contains(@class, "j_readContent")]/p')
    # for i in content:
    #     print(i.xpath('/'))
    # print(content)



    pass


if __name__ == '__main__':
    getdata(base_url)
