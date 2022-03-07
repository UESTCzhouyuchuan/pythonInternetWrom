import time

import requests
from bs4 import BeautifulSoup
from requests import get

from _file import *
from pool import *

requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
s = requests.session()
s.keep_alive = False  # 关闭多余连接


def relateinfoidPageInfo(relateinfoid):
    urlPrefix = "http://ggzyjy.sc.gov.cn/staticJson/"
    ret = {}

    ls = ["503", "514", "504", "517", "506", "511", "513", "512"]

    for item in ls:
        res = get(urlPrefix + relateinfoid + "/" + item + ".json" + "?_=" + str(int(time.time())))
        if (res.status_code == 404):
            ret[item] = None
        else:
            ret[item] = res.json()

    return ret


def getSinglePageInfo(urlEnd, n=None):
    try:
        ret = {}
        urlPrefix = "http://ggzyjy.sc.gov.cn"
        url = urlPrefix + urlEnd
        if n is not None:
            tip = "第" + str(n + 1) + "条数据: " + url + ", "
        else:
            tip = "修复数据：" + url + ", "
        sp = BeautifulSoup(get(url=url).content, features="html.parser", from_encoding="UTF-8")
        relateinfoid = sp.find(attrs={"id": "relateinfoid"})
        if (relateinfoid == None):
            relateinfoid = ""  # 不存在设置为空字符
        else:
            relateinfoid = relateinfoid["data-value"]
        if (relateinfoid == ""):
            print(tip + "relateinfoid为空")
            title = sp.find(attrs={"id": "title"}).string
            detailedDesc = sp.find(class_="detailed-desc").getText()
            newsText = sp.find(attrs={"id": "newsText"}).getText()
            title = ILLEGAL_CHARACTERS(title)
            detailedDesc = ILLEGAL_CHARACTERS(detailedDesc)
            newsText = ILLEGAL_CHARACTERS(newsText)
            ret["title"] = title
            ret["detailedDesc"] = detailedDesc
            ret["newsText"] = newsText
        else:
            print(tip + " relateinfoid = " + relateinfoid)
            ret["relateinfoid"] = relateinfoid
            res = relateinfoidPageInfo(relateinfoid)
            ret = {**ret, **res}
    except Exception as e:
        print(e)
        ret['isError'] = True
    else:
        ret['url'] = url
        return ret


def getAllPagesInfoToJson(key, processNum=10):
    filename_url = './files/' + key + '/url.json'
    fn1 = './files/' + key + '/pages.json'
    fn2 = './files/' + key + '/relateinfoid-pages.json'
    data = readFromFile(filename_url)
    result = pool(data, getSinglePageInfo, processNum)
    pages = []
    relateinfoid_pages = []
    for item in result:
        if 'isError' in item.keys():
            item = getSinglePageInfo(item['url'])
        if item is not None:
            if 'relateinfoid' in item.keys():
                relateinfoid_pages.append(item)
                if item['503'] is not None:
                    t = item['503']['data'][0]
                    data_tmp = {
                        "title": t['title'],
                        "detailedDesc": "发布时间："+t['infoDate'] + " 来源："+t['zhuanzai'] + "原文链接：" + t['originurl'],
                        "newsText": ILLEGAL_CHARACTERS(BeautifulSoup(t['infoContent'], features="html.parser").getText()),
                        'url': item['url']
                    }
                    pages.append(data_tmp)
            else:
                pages.append(item)
    writeToFile(fn1, pages)
    writeToFile(fn2, relateinfoid_pages)
    # print(result[0])
    return result


if __name__ == "__main__":
    key = "四川大学"
    getAllPagesInfoToJson(key, 25)
