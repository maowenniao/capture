import requests
import json
import datetime
import time


def date_change():#定义时间累加函数

    global start_date
    
    td = datetime.timedelta(days=1) #累加1天
    final_date = start_date + td
    d = final_date.__format__('%Y-%m-%d')
    return d

def url_get():#金山词霸每日一句接口网址拼接

    url1 = "http://open.iciba.com/dsapi/?date="
    url2 = date_change()

    url = url1 + url2
    return url

def info_get():#爬取信息，并提取json，写入文档

    url_fin = url_get()

    html = requests.get(url_fin)
    
    jsonData = html.text

    s=json.loads(jsonData)

    content = s['content']#数组中只需要英文原句content,及中文译文note
    note =s['note']
    data = [,"*",content,note,"\n"]

    with open("data.txt",'a',encoding="utf-8") as f:
        f.writelines(data)
    return

if __name__ == '__main__':
    
    start_date = datetime.date(2020,1,1)
    print (start_date)
    for i in range(1,365):
        info_get()
        print (date_change())
        start_date = datetime.datetime.strptime(date_change(), "%Y-%m-%d")
        #time.sleep (1)
        
