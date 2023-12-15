import os

import requests
from lxml import etree


if __name__ == '__main__':
    url="https://sc.chinaz.com/jianli/index.html"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    # 发起请求
    response = requests.get(url=url, headers=header)
    # 设置编码
    response.encoding = 'utf-8'
    # response.encoding='gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    Citys = tree.xpath('//div[@id="main"]/div/div/a/@href')
    if not os.path.exists("./jianliLibs"):
        os.mkdir("./jianliLibs")
    for v in Citys:
        print(v)
        page_text = requests.get(url=v,headers=header).text
        tree2 = etree.HTML(page_text)
        url2 = tree2.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        with open("./jianliLibs/"+url2[-15:],'wb') as fp:
            fp.write(requests.get(url=url2,headers=header).content)