from getAllPagesInfo import getAllPagesInfo
from getAllUrl import getAllUrl
from jsonToXlsx import jsonToXlsx


def main():
    key = "地质灾害"
    # 配置
    config = {
        "chnlNames": '竞争性谈判采购公告',  # 类型
        "chnlCodes": '8a817ecb39d832560139d85973c30b02',  # 类型id
        "distin_like": "510000",  # 市id，如果搜索全省范围值为510000
        "city": "",  # 市名称，如果搜索全省范围则为空
    }
    getAllUrl(key, config)

    getAllPagesInfo(key, 20)

    jsonToXlsx(key)


if __name__ == '__main__':
    main()
