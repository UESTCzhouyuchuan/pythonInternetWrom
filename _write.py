# -*- coding:utf-8 -*-
# 把getAllArticlesPageInfo返回的所有页面的文章信息写道TXT和XLSX中
from _format import *
from _file import *
from getSingleArticleInfo import *

def writeToTxtXlsx(articlesPageInfo,articlesPreInfo):
    # 无双语
    singelNumber = 1
    # 有双语
    notSingleNumber = 1
    # 文件夹前缀
    body_EN = "./resultFile/resultFile/Body/EN-US/"
    body_ZH = "./resultFile/resultFile/Body/ZH-CN/"
    body_Single = "./resultFile/resultFile/Body/Single/"
    # excel文件
    title_Single = "./resultFile/resultFile/Title/Title_Single.xlsx"
    title_EN_ZH = "./resultFile/resultFile/Title/Title_EN_ZH.xlsx"
    index = 0;
    for single_page_info in articlesPageInfo:
        single_pre_info  = articlesPreInfo[index]
        index += 1
        url = single_pre_info["web_url_with_host"]
        type = urlGetType(url)
        date = dateFormat(single_pre_info["publication_date"])
        txtName_EN = body_EN + "Body_EN_" + numberFormat(notSingleNumber, 2) + "_" + date + "_" + type + ".txt"
        txtName_ZH = body_ZH + "Body_ZH_" + numberFormat(notSingleNumber, 2) + "_" + date + "_" + type + ".txt"
        txtName = body_Single + "Body_Single_" + numberFormat(singelNumber, 2) + "_" + date + "_" + type + ".txt"
        # print(date)
        # print(retArticleInfo)
        title_EN = single_page_info["title_EN"]
        title_ZH = single_page_info["title_ZH"]
        isSingle = single_page_info["isSingle"]
        if (isSingle):
            singelNumber += 1
            writeToTxt(txtName, single_page_info["article_paragraph_ZH"])
            writeToXlsx(title_Single, date, title_EN, title_ZH, type, singelNumber)
            # print(txtName)
        else:
            notSingleNumber += 1
            # print(txtName_EN)
            # print(txtName_ZH)
            writeToTxt(txtName_ZH, single_page_info["article_paragraph_ZH"])
            writeToTxt(txtName_EN, single_page_info["article_paragraph_EN"])
            writeToXlsx(title_EN_ZH, date, title_EN, title_ZH, type, notSingleNumber)

def fix(articlesPageInfo,articlesPreInfo):
    index = 0
    sum = 0
    for item in articlesPageInfo:
        if (item == None ):
            url = articlesPreInfo[index]["web_url_with_host"]
            printTip("出现None 需要修复 重新解析网页" + url)
            single_page_info = getURLInfo(url, "")
            articlesPageInfo[index] = single_page_info
            sum += 1;
        index += 1
    return {
        "None": sum,
        "articlesPageInfo": articlesPageInfo
    }
def beginWrite(pageName = "./json/allArticlesPageInfo.json",preName = "./json/allArticlesPreInfo.json"):
    # 读取文件
    articlesPageInfo = getFileData(pageName)
    articlesPreInfo = getFileData(preName)
    ret = fix(articlesPageInfo, articlesPreInfo)
    if (ret["None"] > 0):
        articlesPageInfo = ret["articlesPageInfo"]
        writeToFile(pageName,articlesPageInfo)
        printSuccess("一共"+str(ret["None"])+"个空信息"+"全部修复完成")
    writeToTxtXlsx(articlesPageInfo, articlesPreInfo)
    printSuccess("成功写入TXT和XLSX中")
def main():
    beginWrite()
if __name__ == "__main__":
    main()
