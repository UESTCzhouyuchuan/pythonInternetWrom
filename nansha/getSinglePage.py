from bs4 import BeautifulSoup
import requests
urlPrefix = "https://www.nstimebank.org.cn"
def getSinglePage(url):
    html = requests.get(urlPrefix+url)
    bs = BeautifulSoup(html.text, 'lxml')
    title = bs.find('h2').text
    fbxxs = bs.find_all('p', class_="fbxx")
    desc = bs.find('div', class_="xqnr").text.strip()
    fwnr_p = bs.find('div', class_="fwnr").find_all('p')
    require = fwnr_p[-1].text[5:]
    expirationDate = fwnr_p[-2].text[5:]
    location = fwnr_p[-5].text[5:]
    serviceTime = fwnr_p[-6].text[5:]
    comments = bs.find_all('p', class_="plxx")
    if (comments):
        publisherComment = comments[0].find('font').text[1:-1].strip()
        undertakerComment = comments[1].find('font').text[1:-1].strip()
    else:
        publisherComment = ''
        undertakerComment = ''
    if (len(fbxxs) > 2):
        releaseTime = fbxxs[0].text.split('|')[1].strip()[5:].strip()
        fbxx2 = fbxxs[1].text.split('|')
        timeMoney = fbxx2[4].strip()[7:].strip()
        type = fbxx2[0].strip()[5:].strip()
        fbxx3 = fbxxs[2].text.split("|")
        status = fbxx3[1].strip()[3:].strip()
        undertakeTime = fbxx3[2].strip()[5:]
        finishTime = fbxx3[3].strip()[5:]
    else:
        fbxx1 = fbxxs[0].text.split("|")
        releaseTime = fbxx1[3].strip()[5:].strip()
        timeMoney = fbxx1[2].strip()[6:].strip()
        type = fbxx1[1].strip()[5:].strip()
        fbxx2 = fbxxs[1].text.split("|")
        status = fbxx2[1].strip()[3:].strip()
        undertakeTime = fbxx2[2].strip()[5:]
        finishTime = fbxx2[3].strip()[5:]
    return {
        "title": title,
        "releaseTime": releaseTime,
        "timeMoney": timeMoney,
        "type": type,
        "desc": desc,
        "require": require,
        "expirationDate": expirationDate,
        "location": location,
        "serviceTime": serviceTime,
        "status": status,
        "undertakeTime": undertakeTime,
        "finishTime": finishTime,
        "publisherComment": publisherComment,
        "undertakerComment": undertakerComment
    }

if __name__ == "__main__":
    url = "/timebank/demand/front/indexInfo.action?demandId=86831"
    res = getSinglePage(url)
    print(res)