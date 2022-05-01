import requests
import json

if __name__ == '__main__':
    # step1 指定URL
    post_url = 'https://fanyi.baidu.com/sug'

    # step2 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    # step3 post请求参数处理（同get请求类似）
    word = input('Enter a word:\n')
    data = {
        'kw': word
    }

    # step4 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)

    # step5 获取响应数据:json()方法返回的是obj  (如果确认响应数据是json类型-->通过Content-Type分辨，才可以直接用json方法)
    dict_obj = response.json()
    print(dict_obj)

    # step6 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False)

    print('Over!')