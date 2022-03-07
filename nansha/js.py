import requests
import time
number = 1
cookie = \
    'ASP.NET_SessionId=opvfgwz10w1e2rb3sg4hpmsm; iPlanetDirectoryPro=A9j39PQ01xfXFpC7jGDz0V'
devid = str(103780505+ number)
devName = "S4B001"

timeTag = str(round(time.time() * 1000))
url = "http://reservelib.uestc.edu.cn/ClientWeb/pro/ajax/reserve.aspx?act=set_ResearchSeat&devid="+devid\
      +"&devName="+devName+"&_=" + timeTag

payload = {}
headers = {
  'Cookie': cookie
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)