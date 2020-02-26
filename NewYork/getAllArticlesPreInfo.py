# -*- coding:utf-8 -*-
# 获得查询的关键值返回的所有文章的URL等基本信息
'''
getAllArticlesPreInfo(query = "一带一路",filename = "./json/allArticlesPreInfo.json"):
获得关键字query返回的所有页面的URL等基本信息,写到文件filename中
'''
import requests
from _file import *
from printState import *
from _format import *
def getAllArticlesPreInfo(query = "一带一路",filename = "./json/allArticlesPreInfo.json"):
    # url
    url = 'https://cn.nytimes.com/search/data'
    # 参数
    params = {
        "query": query,
        "lang": "",
        "dt": "json",
        "from": 0,
        "size": 100,
    }
    # 代理
    proxies = {'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
    res = requests.get(url, params=params, proxies=proxies);
    total = json.loads(res.text)["total"]
    # print(total)
    articlesArray = [];
    total = 1246;
    _from = 0;
    _size = 100;
    printTip("开始抓取相关文章的URL")
    while (True):
        res = requests.get(url, params=params, proxies=proxies);
        _from = _from + _size
        params["from"] = _from;
        data = res.text;
        data = json.loads(data, encoding="utf8");
        data = data["items"];
        articlesArray.extend(data);
        if (_from > total):
            break;

        printSuccess("抓取到"+str(_from)+"个URL");
    printSuccess("抓取全部"+str(total)+"个URL")
    articleArray = sorted(articlesArray, key=lambda x: dateFormat(x["publication_date"]))
    # print(articleArray)
    writeToFile(filename,articleArray)
    return articleArray
def main():
    query = "一带一路"
    getAllArticlesPreInfo(query)
if __name__ == "__main__":
    main()
