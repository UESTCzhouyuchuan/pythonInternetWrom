from bs4 import BeautifulSoup
import requests
from myFile import *
url = "https://www.nstimebank.org.cn/timebank/demand/front/index.action"
constYear = "2019"
def getHrefUrl(demandStatus, filename):
    param = {
        "demandStatus": demandStatus,
        "pageNo": 1
    }
    flag = True
    flag1 = True
    res = []
    while (flag):
        html = requests.get(url, params=param)
        bs = BeautifulSoup(html.text, 'lxml')
        xq_titles = bs.find_all('td', class_="xq_title")
        xq_title1s = bs.find_all('td', class_="xq_title1")
        if(flag1):
            if (xq_title1s[9].text.split('|')[2][6:10] > constYear):
                param['pageNo'] += 10;
                continue
            else:
                param['pageNo'] -= 9;
                flag1 = False
                continue
        for index in range(len(xq_titles)):
            year = xq_title1s[index].text.split('|')[2][6:10]
            href = xq_titles[index].find('a')['href']
            printInfo("page: "+str(param['pageNo'])+",year: " + year + ",href:" + href)
            if (year > constYear):
                continue
            elif (year < constYear):
                flag = False
                break
            else:
                res.append(href)
        param['pageNo'] += 1
    writeToFile(filename, res)

if __name__ == "__main__":
    getHrefUrl(7, "expiredHref.json")