
from getAllUrl import getAllUrl
from getAllPagesInfoToJson import getAllPagesInfoToJson
from JsonToXlsx import JsonToXlsx

def main():
    # 关键字
    key = "地质灾害"

    # 获得url,自动写入文件
    getAllUrl(key)

    # 获得全部url中的数据，并写入文件中
    getAllPagesInfoToJson(key, 20)
    # 写入xlsx中
    JsonToXlsx(key)

if __name__ == '__main__':
    main()