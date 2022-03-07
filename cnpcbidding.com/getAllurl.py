import os

from requests import post

from encrypt import *
from tools import pool

Page_Size = 100


def getUrl(key, pageNum=1):
    try:
        url = 'https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
        }
        userData = {'pageSize': 15,
                    'title': key,
                    'pageNo': pageNum,
                    'pid': 198,
                    'categoryId': 199,
                    'projectType': ''
                    }
        tip = f'爬取key={key},第{pageNum}页的url'
        data = encrypt_data(userData)
        data_str = json.dumps(data)
        response = post(url, data=data_str, headers=headers)
        data = response.json()
        if 'msg' in data.keys():
            printTip(data)
        response.close()
        # printTip(f'密文: {data}')
        ret = decrypt_data(data)
        # printTip(f'明文：{ret}')
        printTip(tip)
        return ret
    except Exception as e:
        traceback.print_exc()


def getAllUrls(key):
    dic = f'./files/{key}/'
    if not os.path.exists(dic):
        os.mkdir(dic)
    urls = []
    result = getUrl(key)
    urls.extend(result['list'])
    total = result['total']
    page_size = Page_Size
    args = []
    for i in range(2, total // page_size + 1):
        args.append((key, i))
    if args:
        results = pool(args, getUrl, 20)
        for item in results:
            urls.extend(item['list'])
    printSuccess(f'爬取关键字为{key}的全部url')
    writeToFile(f'{dic}url.json', urls)
    return urls

if __name__ == '__main__':
    # st = ''
    # for i in range(10):
    #     st += '电'
    #     ret = getAllUrls(st)
    getAllUrls('四川大学')