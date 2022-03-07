
from _file import *

def jsonToXlsx(key):
    dic = "./files/" + key
    data = readFromFile(dic + '/result.json')

    type_1 = []
    headers1 = ['title', 'time', 'myPrintArea', 'attachment', 'url']
    type_2 = []
    headers2 = ['title', 'project_number', 'content', 'url']
    for item in data:
        if item['type'] == 2:
            type_2.append(item)
        else:
            type_1.append(item)

    writeToXlsx(dic + '/result1.xlsx', type_1, headers1)
    writeToXlsx(dic + '/result2.xlsx', type_2, headers2)
if __name__ == '__main__':
    jsonToXlsx('地质灾害')