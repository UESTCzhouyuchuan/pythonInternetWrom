import json
from bs4 import BeautifulSoup


def writeToJSon(data, filename="emojis.json"):
    try:
        file = open(filename, mode='w', encoding="utf8")
    except Exception:
        print("Error can't open")
    else:
        file.write(str(json.dumps(data, ensure_ascii=False, indent=2)))
        file.flush()
        file.close()
        print('数据写入文件' + filename)


def getImgSrc(item):
    img = item.img
    if (img):
        return img["src"]
    else:
        return ""


def getAndr(item):
    ret = {}
    imgs = item.find_all("img", class_="imga new", recursive=False)
    for x in imgs:
        ret[x["title"]] = x["src"]
    return ret;


def printJson(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def consult(item):
    ret = {
        "is_rcharts": False,
        "bighead": "",
        "bighead_url": "",
        "mediumhead": "",
        "mediumhead_url": "",
        "number": "",
        "Code": "",
        "Browser": "",
        "Apple": "",
        "Google": "",
        "FaceBook": "",
        "Windows": "",
        "Twitter": "",
        "Joy": "",
        "Sama": "",
        "GMail": "",
        "SB": "",
        "DCM": "",
        "KDDI": "",
        "CLDR-Short-Name": "",
        "andr": ""
    }
    # print(item)
    th = item.th
    if (th):
        th_class = th["class"][0]
        # print(th_class)
        if (th_class == "rchars"):
            ret["is_rcharts"] = True
        elif (th_class == "bighead"):
            ret["bighead"] = th.text
            ret["bighead_url"] = th.a["href"]
        else:
            ret["mediumhead"] = th.text
            ret["mediumhead_url"] = th.a["href"]
    else:
        ths = item.contents
        # 清除"\n"
        ths = [item for item in ths if item != "\n"]
        # print(ths)
        ret["number"] = ths[0].text
        ret["Code"] = ths[1].a["name"]
        ret["Browser"] = ths[2].text
        if (len(ths) <= 5):
            ret["andr"] = getAndr(ths[3])
            # printJson(ret["andr"])
            ret["CLDR-Short-Name"] = ths[4].text
        else:
            ret["Apple"] = getImgSrc(ths[3])
            ret["Google"] = getImgSrc(ths[4])
            ret["FaceBook"] = getImgSrc(ths[5])
            ret["Windows"] = getImgSrc(ths[6])
            ret["Twitter"] = getImgSrc(ths[7])
            ret["Joy"] = getImgSrc(ths[8])
            ret["Sama"] = getImgSrc(ths[9])
            ret["GMail"] = getImgSrc(ths[10])
            ret["SB"] = getImgSrc(ths[11])
            ret["DCM"] = getImgSrc(ths[12])
            ret["KDDI"] = getImgSrc(ths[13])
            ret["CLDR-Short-Name"] = ths[14].text
    return ret

def getDataFromHtml(filename):
    try:
        html = BeautifulSoup(open(filename, encoding='utf-8'), features='html.parser')
    except Exception as e:
        print(str(e))
    trs = html.find_all("tr")
    # res = consult(trs[194])
    # printJson(res)
    # return
    # josn数据
    data = []
    i = 0;
    bighead = ""
    mediumhead = "";
    for item in trs:
        res = consult(item)
        if (res["is_rcharts"]):
            continue
        elif (res["bighead"]):
            bighead = res["bighead"]
            bighead_url = res["bighead_url"]
        elif (res["mediumhead"]):
            mediumhead = res["mediumhead"]
            mediumhead_url = res["mediumhead_url"]
        else:
            if (res["andr"]):
                t = {"bighead": bighead, "bighead_url": bighead_url, "mediumhead": mediumhead,
                     "mediumhead_url": mediumhead_url,
                     "number": res["number"],
                     "Code": res["Code"],
                     "Browser": res["Browser"],
                     "Code": res["Code"],
                     "Browser": res["Browser"],
                     "Apple": "",
                     "Google": "",
                     "FaceBook": "",
                     "Windows": "",
                     "Twitter": "",
                     "Joy": "",
                     "Sama": "",
                     "GMail": "",
                     "SB": "",
                     "DCM": "",
                     "KDDI": "",
                     "CLDR-Short-Name": res["CLDR-Short-Name"],
                     "andr": res["andr"]}
            else:
                t = {"bighead": bighead, "bighead_url": bighead_url, "mediumhead": mediumhead,
                     "mediumhead_url": mediumhead_url,
                     "number": res["number"],
                     "Code": res["Code"],
                     "Browser": res["Browser"],
                     "Apple": res["Apple"],
                     "Google": res["Google"],
                     "FaceBook": res["FaceBook"],
                     "Windows": res["Windows"],
                     "Twitter": res["Twitter"],
                     "Joy": res["Joy"],
                     "Sama": res["Sama"],
                     "GMail": res["GMail"],
                     "SB": res["SB"],
                     "DCM": res["DCM"],
                     "KDDI": res["KDDI"],
                     "CLDR-Short-Name": res["CLDR-Short-Name"],
                     "andr": ""
                     }
            data.append(t)
        i += 1
        print("成功分析第" + str(i) + "行数据")
    jsonName = filename.split('.html')[0] + ".json"
    writeToJSon(data, jsonName);
def main():
    getDataFromHtml("./skin-tones-emojis-v13.0.html")

if __name__ == "__main__":
    main()