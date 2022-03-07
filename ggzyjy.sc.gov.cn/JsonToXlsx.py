from _file import *

def JsonToXlsx(key):
    filename = './files/' + key + '/pages.json'
    all_pages = readFromFile(filename)
    writeToXlsx('./files/' + key+"/pages.xlsx", all_pages)


if __name__ == "__main__":
    JsonToXlsx('四川大学')