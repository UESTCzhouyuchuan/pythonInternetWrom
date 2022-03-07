# -*- coding: utf-8 -*-
import datetime
import os

import requests

from _file import *

url = "http://ggzyjy.sc.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.182 Safari/537.36",
}


def getTotalCount(json_data):
    response = requests.post(url=url, headers=headers, json=json_data)
    data = response.json()
    return data['result']['totalcount']


def getAllUrl(key):
    fn = "./files/" + key + '/url.json'
    today = datetime.date.today()
    endTime = today.strftime("%Y-%m-%d") + " 23:59:59"
    startTime = today.replace(month=today.month - 1).strftime("%Y-%m-%d") + " 00:00:00"
    print(startTime, endTime)
    json_data = {
        "token": "",
        "pn": 0,
        "rn": '',
        "sdt": "",
        "edt": "",
        "wd": key,
        "inc_wd": "",
        "exc_wd": "",
        "fields": "title",
        "cnum": "",
        "sort": "{'webdate':'0'}",
        "ssort": "title",
        "cl": 500,
        "terminal": "",
        "condition": [
            {
                "fieldName": "categorynum",
                "equal": "002001",
                "notEqual": None,
                "equalList": None,
                "notEqualList": None,
                "isLike": True,
                "likeType": 2
            }
        ],
        "time": [
            {
                "fieldName": "webdate",
                "startTime": startTime,
                "endTime": endTime
            }
        ],
        "highlights": "",
        "statistics": None,
        "unionCondition": None,
        "accuracy": "",
        "noParticiple": "0",
        "searchRange": None,
        "isBusiness": "1"
    }
    totoal_count = getTotalCount(json_data)
    print("共{}条数据".format(totoal_count))
    json_data['rn'] = totoal_count
    response = requests.post(url=url, headers=headers, json=json_data)
    data = response.json()
    data = data['result']['records']
    print("成功获得页面的全部url")
    if (os.path.exists('./files/' + key) is not True):
        os.mkdir('./files/' + key)
    writeToFile(fn, data)

    return data


def main():
    key = "地质灾害"
    getAllUrl(key)


if __name__ == '__main__':
    main()
