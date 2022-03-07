import os

from bs4 import BeautifulSoup
from requests import get

from _file import *

user_config = {
    "chnlNames": '',
    "chnlCodes": '',
    "distin_like": "510000",
    "city": "",
}


def pages(key, page, config):
    url = "http://www.ccgp-sichuan.gov.cn/CmsNewsController.do"
    try:
        json_data = {
            "method": "search",
            **config,
            "tenderno": '',
            "agentname": '',
            "buyername": '',
            "startTime": '',
            "endTime": '',
            "town": '',
            "pageSize": 10,
            "searchResultForm": "search_result_anhui.ftl",
            "title": key,
            "curPage": page,
            "province": 510000,
            "provinceText": "四川省",
            "cityText": "四川省",
            "townText": "四川省"
        }
        response = get(url=url, params=json_data)
        # print(response.url)
        bs = BeautifulSoup(response.content, features="html.parser", from_encoding="UTF-8")
        response.close()
        print(f'爬取第{page}页')
        ret = []
        for item in bs.select('.list-info .info ul a'):
            ret.append(item['href'])
        print(ret)
        return ret
    except Exception as e:
        print(f'{url}:{key}:{page}:{e}')


def getAllUrl(key, config=user_config):
    url = "http://www.ccgp-sichuan.gov.cn/CmsNewsController.do"
    try:
        # 竞争性谈判采购公告
        jsonData = {
            "method": "search",
            **config,
            "tenderno": '',
            "agentname": '',
            "buyername": '',
            "startTime": '',
            "endTime": '',
            "town": '',
            "pageSize": 10,
            "searchResultForm": "search_result_anhui.ftl",
            "title": key,
            "province": 510000,
            "provinceText": "四川省",
            "cityText": "四川省",
            "townText": "四川省"
        }
        response = get(url=url, params=jsonData)
        # print(response.text)
        bs = BeautifulSoup(response.content, features="html.parser", from_encoding="UTF-8")
        response.close()
        ret = []
        for item in bs.select('.list-info .info ul a'):
            ret.append(item['href'])
        print('爬取第一页')
        print(ret)
        page_num = bs.find('a', title="尾页", string="尾页")
        if page_num is not None:
            page_num = int(page_num['id'])
            for i in range(1, page_num):
                ret.extend(pages(key, i + 1, config))
        dic = './files/' + key
        if os.path.exists(dic) is not True:
            os.mkdir(dic)
        print("爬取全部url")
        writeToFile(dic + '/url.json', ret)
        return ret
    except Exception as e:
        print(url, e)


if __name__ == '__main__':
    getAllUrl("地质灾害")
