import json

import requests

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"
    # UA伪装
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    header = {
        'User-Agent': UA
    }
    # post请求
    param = {
        'kw':'dog'
    }
    response = requests.post(url=url,data=param,headers=header)
    print(response.json())
    data = response.json()
    file = open("fanyi.txt",'w',encoding="utf-8")
    # json数据持久化，不使用ascii编码
    json.dump(data,fp=file,ensure_ascii=False)