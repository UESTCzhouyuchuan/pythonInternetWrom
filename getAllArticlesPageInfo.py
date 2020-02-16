# -*- coding:utf-8 -*-
# 获得全部页面文章信息
'''
默认打开./json/allArticlesPreInfo.json文件，获得每个页面的URL等基本信息，放到列表articlesPreInfo中
再提取所有页面的文章信息，放到列表articlesPageInfo中
列表articlesPageInfo和articlesPreInfo相同index处对应同一篇文章。
相关函数：
allArticles(articlesPreInfo, start):提取列表articlesPreInfo的全部文章信息，返回结果列表
getAllArticlesPageInfo(openfilename,writefilename):以多进程提取URL中的文章,把结果写到writefilename中
openfilename默认值是"./json/allArticlesPreInfo.json",writefilename默认值是"./json/allArticlesPageInfo.json"
'''
from multiprocessing import Pool
from _file import *
from getSingleArticleInfo import *


def allArticles(articlesPreInfo, start):
    articlesPageInfo = []
    for article in articlesPreInfo:
        url = article["web_url_with_host"]
        retArticleInfo = getURLInfo(url, start + 1)
        # print(retArticleInfo)
        articlesPageInfo.append(retArticleInfo)
        start += 1
    return articlesPageInfo


def getAllArticlesPageInfo(openfilename="./json/allArticlesPreInfo.json",
                           writefilename="./json/allArticlesPageInfo.json"):
    articlesPreInfo = getFileData(openfilename)
    articlesList_Len = len(articlesPreInfo)
    printInfo("一共" + str(articlesList_Len) + "篇文章")
    pian = 10  # 进程数量，视cpu性能修改
    ariclesSplit = [[0] for i in range(pian)]
    for x in range(pian):
        ariclesSplit[x] = articlesPreInfo[
                          (x * articlesList_Len // pian):(articlesList_Len + (x * articlesList_Len)) // pian]
    for x in range(pian):
        printInfo("第" + str(x + 1) + "进程文章数量：" + str(len(ariclesSplit[x])))
    printInfo("开始爬取....")
    start = 0;
    p = Pool(pian)
    canshu = []
    for articles in ariclesSplit:
        canshu.append((articles, start))
        start += len(articles)
    ret = p.starmap(allArticles, canshu)
    articlesPageInfo = []
    for item in ret:
        articlesPageInfo.extend(item)
    printSuccess("爬取所有页面的文章信息")
    # 写到文件中
    writeToFile(writefilename, articlesPageInfo)
    return articlesPageInfo


def main():
    openfilename = "articles.json"
    # 获得所有页面信息
    articlesPageInfo = getAllArticlesPageInfo()


if __name__ == "__main__":
    main()
