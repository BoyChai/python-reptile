import requests
from lxml import etree

if __name__ == '__main__':
    url="https://www.aqistudy.cn/historydata/"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    # 发起请求
    response = requests.get(url=url, headers=header)
    # 设置编码
    response.encoding='utf-8'
    # response.encoding='gbk'
    page_text = response.text
    tree= etree.HTML(page_text)
    Citys = tree.xpath('//div[@class="all"]/div[@class="bottom"]//li/a/text()')
    for city in Citys:
        print(city)
