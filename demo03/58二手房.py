import requests
from lxml import etree

if __name__ == '__main__':
    url="https://wf.58.com/ershoufang/"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    # 发起请求
    page_text = requests.get(url=url,headers=header).text
    tree= etree.HTML(page_text)
    titles = tree.xpath("//div//h3[@class='property-content-title-name']/text()")
    prices = tree.xpath("//span[@class='property-price-total-num']/text()")
    for i in range(0,len(titles)):
        print(titles[i]+" "+prices[i])
