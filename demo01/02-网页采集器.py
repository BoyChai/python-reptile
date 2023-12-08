import requests


# UA伪装
# UA: User-Agent请求载体(请求载体的身份标识)
# 伪装浏览器发起请求
if __name__ == "__main__":
    url="https://www.sogou.com/web"
    # 封装参数
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    # UA伪装
    # Google Chrom浏览器
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    header = {
        'User-Agent':UA
    }
    # 请求
    # 如果不加这个UA伪装的header则请求会被拦截要求认证
    # response = requests.get(url=url,params=param)
    response = requests.get(url=url,params=param,headers=header)
    print(response.text)
    # 保存数据
    filename=kw+".html"
    with open(filename,'w',encoding="utf-8") as fp:
        fp.write(response.text)