import json

import requests

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"

    param = {
        'type': '24', # 类型
        'interval_id': '100:90', # 评分
        'action':'',
        'start': '0', # 从第几个开始
        'limit': '100', # 请求数量
    }
    # UA伪装
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    header = {
        'User-Agent': UA
    }
    response = requests.get(url=url,params=param,headers=header)

    list_data = response.json()
    fp = open("./douban.txt",'w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)