# -*- coding:utf-8 -*-
# 主函数
from getAllArticlesPreInfo import *
from getAllArticlesPageInfo import *
from _write import *
def main():
    query = "一带一路"
    getAllArticlesPreInfo()
    getAllArticlesPageInfo()
    beginWrite()
if __name__ == "__main__":
    main()