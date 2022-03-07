# -*- coding:utf-8 -*-
# 封装输出格式化
'''
printError(_str):输出错误信息
printSuccess(_str):输出执行成功的提示信息
printInfo(_str):输出普通信息
printTip(_str):输出提示信息
'''


def printError(_str):
    print("\033[1;31mError：{}出现错误\033[0m".format(_str))


def printSuccess(_str):
    print("\033[1;32mSuccess：{}成功\033[0m".format(_str))


def printInfo(_str):
    print("\033[1;34mInfo：{}\033[0m".format(_str))


def printTip(_str):
    print("\033[0;36mIip：{}\033[0m".format(_str))


if __name__ == "__main__":
    filename = "test.txt"
    printInfo('写入文件' + filename)
    printTip('写入文件' + filename)