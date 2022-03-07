import http.client
import mimetypes
conn = http.client.HTTPSConnection("cn.nytimes.com")
payload = ''
headers = {
  'Cookie': 'nytimes_sec_token=88370adea135743b78e53049d4effe4e; NYTCN-MSS=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22822635d95dc71d0dafba1776283c1f6d%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%2210.9.151.58%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A17%3A%22Amazon+CloudFront%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1603195574%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dc6f1e542abb56de55626c3356489c11ff1ec6d54; AWSALB=1njZT8MJfA4sP9czBZbBwPzT1Rw3dRmM1frVTqfl6YSMRXsRIrhxGxT9Osf+pzdtJZwPsWin+ZYoe4s1ETGEPq1jL+FxL/oT6kPtgbijYdqAiSa2ixQAKaKW0gS6; AWSALBCORS=1njZT8MJfA4sP9czBZbBwPzT1Rw3dRmM1frVTqfl6YSMRXsRIrhxGxT9Osf+pzdtJZwPsWin+ZYoe4s1ETGEPq1jL+FxL/oT6kPtgbijYdqAiSa2ixQAKaKW0gS6'
}
conn.request("GET", "/search/data/?query=covid-19&lang=&dt=json&from=0&size=10", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))