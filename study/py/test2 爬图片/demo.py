import requests
from pyquery import PyQuery as pq
import time
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
url = "http://www.netbian.com/desk/22500-1920x1080.htm"


r = requests.get(url, headers=headers)
# 这个网站页面使用的是GBK编码 这里进行编码转换
r.encoding = 'GBK'
html = r.text

# print(html)
doc = pq(html)
print(doc('div.list').items())



