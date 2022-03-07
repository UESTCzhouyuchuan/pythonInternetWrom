import requests
import time
import schedule
def main():
    number = 10
    cookie = \
        'ASP.NET_SessionId=1rua553uc1npc14ik20hbjcr; iPlanetDirectoryPro=nqVvU7cd9dy3nZsOGxSdPr'
    devid = str(103780505 + number)
    devName = "S4B010"

    timeTag = str(round(time.time() * 1000))
    url = "http://reservelib.uestc.edu.cn/ClientWeb/pro/ajax/reserve.aspx?act=set_ResearchSeat&devid=" + devid \
          + "&devName=" + devName + "&_=" + timeTag

    payload = {}
    headers = {
        'Cookie': cookie
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

schedule.every().day.at("23:34").do(main,)