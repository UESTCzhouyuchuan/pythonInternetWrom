from multiprocessing import Pool

from printState import *

def pool(data, cb, processNumn=10):
    try:
        printTip(f"开始多进程,一共{len(data)}个数据, {processNumn}个进程")
        printTip("开始爬取....")
        p = Pool(processNumn)
        ret = p.starmap(cb, data)
        printSuccess("成功爬取所有数据")
        return ret
    except Exception as e:
        printError(f"开启多进程, error: {e}")
