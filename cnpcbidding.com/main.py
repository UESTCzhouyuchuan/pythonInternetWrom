from getAllPages import getAllPages
from getAllurl import getAllUrls
from tools import *


def main():
    key = "地质灾害"
    urls = getAllUrls(key)
    if urls:
        getAllPages(key)
    else:
        printTip("未查到相关数据")


if __name__ == '__main__':
    main()
