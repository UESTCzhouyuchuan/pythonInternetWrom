# -*- coding:utf-8 -*-
# 获得单个URL的文章信息，返回结果
import requests
from printState import *
from pyquery import PyQuery as pq


def getURLInfo(url, number):
    # 代理
    proxies = {'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
    payload = {}
    headers = {}
    backFix = "dual/"
    realURL = url + backFix
    try:
        response = requests.request("GET", realURL, headers=headers, data=payload, proxies=proxies)
    except Exception as e:
        printError("解析网页" + realURL + str(e))
    else:
        doc = pq(response.text)
        notFound = doc("head title")
        isSingle = ''
        if (notFound.text() == "页面没有找到 - 纽约时报中文网"):
            isSingle = True
            try:
                response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
            except Exception as e:
                printError("解析网页" + url + str(e))
            else:
                doc = pq(response.text)
                title_ZH = doc('.article-header header h1:first-of-type').text()
                title_EN = ""
                article_paragraph_ZH = []
                article_paragraph_EN = []
                article_paragraph_items = doc('.article-paragraph').items()
                for item in article_paragraph_items:
                    article_paragraph_ZH.append(item.text())
                printInfo("处理第" + str(number) + "篇文章:" + url + "结果如下：")
                printTip("该篇无双语版")
                printSuccess("解析该网页")
                return {
                    "isSingle": isSingle,
                    "title_ZH": title_ZH,
                    "title_EN": title_EN,
                    "article_paragraph_ZH": article_paragraph_ZH,
                    "article_paragraph_EN": article_paragraph_EN
                }
        else:
            isSingle = False
            # print("得到网页源码")
            title_ZH = doc('.article-header header h1:first-of-type').text()
            title_EN = doc('.article-header header h1.en-title').text()
            article_paragraph_ZH = []
            article_paragraph_EN = []
            article_paragraph_items = doc('.article-paragraph').items()
            ZH = False
            for item in article_paragraph_items:
                if (ZH):
                    article_paragraph_ZH.append(item.text())
                else:
                    article_paragraph_EN.append(item.text())
                ZH = not ZH
            printInfo("处理第" + str(number) + "篇文章:" + url + "结果如下：")
            printTip("该篇存在双语版")
            printSuccess("解析网页" + realURL)
            return {
                "isSingle": isSingle,
                "title_ZH": title_ZH,
                "title_EN": title_EN,
                "article_paragraph_ZH": article_paragraph_ZH,
                "article_paragraph_EN": article_paragraph_EN
            }


def getURLInfo_(url):
    # 代理
    proxies = {'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
    payload = {}
    headers = {}
    backFix = "dual/"
    realURL = url + backFix
    try:
        response = requests.request("GET", realURL, headers=headers, data=payload, proxies=proxies)
    except Exception as e:
        printError("解析网页" + realURL + str(e))
    else:
        doc = pq(response.text)
        notFound = doc("head title")
        isSingle = ''
        if (notFound.text() == "页面没有找到 - 纽约时报中文网"):
            isSingle = True
            try:
                response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
            except Exception as e:
                printError("解析网页" + url + str(e))
            else:
                doc = pq(response.text)
                title_ZH = doc('.article-header header h1:first-of-type').text()
                title_EN = ""
                article_paragraph_ZH = []
                article_paragraph_EN = []
                article_paragraph_items = doc('.article-paragraph').items()
                for item in article_paragraph_items:
                    article_paragraph_ZH.append(item.text())
                printTip("弥补处理文章:" + url + "结果如下：")
                printTip("该篇无双语版")
                printSuccess("解析该网页")
                return {
                    "isSingle": isSingle,
                    "title_ZH": title_ZH,
                    "title_EN": title_EN,
                    "article_paragraph_ZH": article_paragraph_ZH,
                    "article_paragraph_EN": article_paragraph_EN
                }
        else:
            isSingle = False
            # print("得到网页源码")
            title_ZH = doc('.article-header header h1:first-of-type').text()
            title_EN = doc('.article-header header h1.en-title').text()
            article_paragraph_ZH = []
            article_paragraph_EN = []
            article_paragraph_items = doc('.article-paragraph').items()
            ZH = False
            for item in article_paragraph_items:
                if (ZH):
                    article_paragraph_ZH.append(item.text())
                else:
                    article_paragraph_EN.append(item.text())
                ZH = not ZH
            printTip("弥补处理文章:" + url + "结果如下：")
            printTip("该篇存在双语版")
            printSuccess("解析网页" + realURL)
            return {
                "isSingle": isSingle,
                "title_ZH": title_ZH,
                "title_EN": title_EN,
                "article_paragraph_ZH": article_paragraph_ZH,
                "article_paragraph_EN": article_paragraph_EN
            }


def main():
    single_url = "https://cn.nytimes.com/health/20121011/cc11patient/"
    not_single_url = "https://cn.nytimes.com/travel/20131018/t18qingdao"
    data = getURLInfo(not_single_url,100)
    # print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
