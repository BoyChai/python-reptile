import  requests

if __name__ == "__main__":
    # 指定URL地址
    url="https://www.sogou.com/"
    # 发起GET请求
    response = requests.get(url=url)
    # 输入返回内容
    print(response.text)
    # 保存数据
    with open("./sogou.html",'w',encoding="utf-8") as fp:
        fp.write(response.text)