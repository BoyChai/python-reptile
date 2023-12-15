import os.path

import requests
from lxml import etree

if __name__ == '__main__':
    url="https://pic.netbian.com/4kmeinv/"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    # 发起请求
    response = requests.get(url=url, headers=header)
    # 设置编码
    # response.encoding='utf-8'
    response.encoding='gbk'
    page_text = response.text
    tree= etree.HTML(page_text)
    # 创建文件夹
    if not os.path.exists("./picLibs"):
        os.mkdir("./picLibs")
    urls = tree.xpath('//*[@id="main"]/div/ul/li/a/img/@src')
    names = tree.xpath('//*[@id="main"]/div/ul/li/a/img/@alt')
    for i in range(0,len(urls)):
        print(names[i]+" "+"https://pic.netbian.com"+urls[i])
        img_url = "https://pic.netbian.com"+urls[i]
        img_path = "./picLibs/"+names[i]+".jpg"
        with open(img_path,'wb') as fp:
            img_data = requests.get(url=img_url, headers=header).content
            fp.write(img_data)