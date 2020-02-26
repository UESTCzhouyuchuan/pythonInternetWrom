# -*- coding:utf-8 -*-
# 格式化操作
'''
包括：
numberFormat(number,length):把number转化为长度length，不足前面补零
dateFormat(date):把年月日格式转化为数字格式，例如2019年1月1日格式化为20190101
urlGetType(url):截取url一部分获得文章类型
'''
import re
def numberFormat(number,length):
    number = int(number)
    _str = "{:0>"+ str(length)+"d}";
    return str(_str.format(number))
def dateFormat(date):
    date = re.split('[^\d]+', date)
    date = date[0] + numberFormat(date[1], 2) + numberFormat(date[2], 2)
    return date
def urlGetType(url):
    arr = re.split('/',url);
    return arr[3].capitalize();
if __name__ == "__main__":
    ret = urlGetType("https://cn.nytimes.com/health/20121011/cc11patient/")
    print(ret)
    print(type(ret))