# -*- coding:utf-8 -*-
# 根据需求更改文档内容
import os
import re
from printState import *
def readFile(filename):
    f = open(filename,"r",encoding="utf8");
    ret = "".join(f.readlines())
    f.close()
    return ret
def consult(filename,index):
    str_ = readFile(filename)
    # print(str_)
    f = open(filename,mode="w",encoding="utf-8")
    data = re.sub("\([a-zA-Z\s\.]*\)","",str_)
    # print(data)
    f.write(data);
    f.flush()
    f.close()
    printSuccess("处理第"+str(index)+"个文件")
def main():
    os.chdir("./ZH-CN/ZH-CN")
    files = os.listdir()
    files_len = len(files)
    for i in range(1,files_len):
        consult(files[i],i)
if __name__ == "__main__":
    main()