from multiprocessing import Pool
from myPrint import *
from myFile import *
from getSinglePage import *
def all(arr, start):
    ret = []
    for item in arr:
        if(item.split('/')[2] == "active"):
            printInfo("第" + str(start) + "条数据被过滤")
            start +=1;
            continue
        try:
            t = getSinglePage(item)
        except Exception as e:
            printError("爬第"+str(start) + "条数据"+item + str(e) )
        else:
            printSuccess("爬第" + str(start) + "条数据")
        ret.append(t)
        start +=1
    return ret
def getAll(jsonRead):
    urlData = getFileData(jsonRead)
    dataLen = len(urlData)
    printInfo("一共" + str(dataLen) + "条数据")
    pian = 10  # 进程数量，视cpu性能修改
    dataSplit = [[0] for i in range(pian)]
    for x in range(pian):
        dataSplit[x] = urlData[
                          (x * dataLen // pian):(dataLen + (x * dataLen)) // pian]
    for x in range(pian):
        printInfo("第" + str(x + 1) + "进程数据数量：" + str(len(dataSplit[x])))
    printInfo("开始爬取....")
    p = Pool(pian)
    args = []
    start = 1
    for data in dataSplit:
        args.append((data,start))
        start += len(data)
    allData = p.starmap(all, args)
    ret = []
    for item in allData:
        ret.extend(item)
    printSuccess("爬取所有页面的文章信息")
    return ret
def getAllDataWriteToFile(jsonName, xlsxName):
    data = getAll(jsonName)
    writeToXlsx(xlsxName, data)
if __name__ == "__main__":
    getAllDataWriteToFile('expiredHref.json', 'expired.xlsx')