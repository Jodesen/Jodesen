import requests

city = {'北京': '101010100',
        '济南': '101120101',
        '青岛': '101120201',
        '淄博': '101120301',
        '烟台': '101120501',
        '潍坊': '101120601',
        '曲阜': '101120710',
        '泰安': '101120801',
        '滨州': '101121101'}

cityname = input('输入查询城市:')
citycode = city[cityname]
url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=%s' % citycode
# print('城市：{}，编号：{}'.format(cityname,citycode))
# print(url)

res = requests.get(url)
info = res.json()
print(info)
data = info['data']
weatherItems = data['forecast']
today = weatherItems[0]
print(weatherItems[1])

city = f"【城市:{data['city']}】\n"
date = f"日期:{today['date']}\n"
now = f"实时温度:{data['wendu']}度\n"
tips = f"今日贴士:{data['ganmao']}\n"
print(city, date, now, tips)

print('【未来4日天气情况:】\n')
for today in weatherItems[1:]:
    # today = data['forecast'][0]
    date = f"日期:{today['date']}"
    temperature = f"温度:{today['high']} {today['low']}"
    weatherType = f"天气:{today['type']}"
    fengxiang = f"风向:{today['fengxiang']}"
    fengli = str(f"风力:{today['fengli']}")
    a = fengli[12:15]
    print('{}, {}, {},{}{}\n'.format(date, weatherType, temperature,fengxiang,a))
