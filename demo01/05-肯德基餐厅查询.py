import json

import requests

if __name__ == "__main__":
    url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

    param = {
        'cname':'北京', # 地区
        'pid':'',
        'keyword': '延庆', # 关键词
        'pageIndex': '1', # 从第几个开始
        'pageSize': '10', # 获取的数量
    }
    # UA伪装
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    header = {
        'User-Agent': UA,
        'Content-Type':'text/plain;charset=utf-8',
    }
    response = requests.post(url=url,params=param,headers=header)
    print(response.text)
    list_data = response.json()
    fp = open("./kendeji.txt",'w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)