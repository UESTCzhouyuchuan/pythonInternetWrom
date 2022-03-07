from requests import post

from encrypt import *
from bs4 import BeautifulSoup

def getSinglePage(url_data, index=None):
    id = url_data['id']
    if index is None:
        tip = f'修补数据: id={id}'
    else:
        tip = f'爬取第{index}条数据,id={id}'
    try:
        url = 'https://www.cnpcbidding.com/cms/pmsbidInfo/detailsOut'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type': 'application/json;charsetset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
        }
        user_data = {'pid': 198, 'categoryId': 199, 'dataId': id}
        data = encrypt_data(user_data)
        data_str = json.dumps(data)
        response = post(url, data=data_str, headers=headers)
        data = response.json()
        response.close()
        result = decrypt_data(data)
        printSuccess(tip)
        attachment_list = []
        for item in result['attachmentList']:
            attachment_list.append({
                "name": item['NAME'],
                "url": f"https://www.cnpcbidding.com/pmsbid/download?id={item['ATTACHMENTID']}&skip=true",
            })
        myret = {
            "attachmentList": attachment_list,
            **result['list'][0],
            "content": ILLEGAL_CHARACTERS(BeautifulSoup(result['list'][0]['bulletincontent'], features="html.parser").get_text())
        }
        return myret
    except Exception as e:
        printError(f'ErrorId={id}')
        traceback.print_exc()


def getAllPages(key):
    dic = f'./files/{key}/'
    urls = readFromFile(f'{dic}url.json')
    args = []
    for i in range(len(urls)):
        args.append((urls[i], i + 1))
    result = pool(args, getSinglePage, 20)
    writeToFile(f'{dic}result.json', result)
    writeToXlsx(f'{dic}result.xlsx', result)
    return result
if __name__ == '__main__':
    ret = getAllPages('地质灾害')