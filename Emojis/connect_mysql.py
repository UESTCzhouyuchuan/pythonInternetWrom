import mysql.connector as mc
import json


# import gzip
def readFileJson(filename):
    try:
        with open(filename, encoding="utf8") as f:
            ret = json.load(f)
    except Exception as e:
        print(str(e))
    else:
        return ret


def fromJsonToMysql(filename, table="emojis"):
    emojis = readFileJson(filename);
    db = mc.connect(host="49.233.169.5", user="yuchuan", password="081849", database="study", charset="utf8mb4")
    cur = db.cursor()
    index = 1;
    for item in emojis:
        cur.execute(
            "INSERT INTO %s" % table + "(number,code,bighead,bighead_url,mediumhead,mediumhead_url,browser,apple,google,"
                                       "facebook,windows,twitter,joy,sams,gmail,sb,dcm,kddi,cldr_short_name,andr) "
                                       "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (item["number"], item["Code"], item["bighead"], item["bighead_url"], item["mediumhead"],
             item["mediumhead_url"], item["Browser"], item["Apple"], item["Google"], item["FaceBook"],
             item["Windows"], item["Twitter"], item["Joy"], item["Sama"], item["GMail"], item["SB"],
             item["DCM"], item["KDDI"], item["CLDR-Short-Name"], json.dumps(item["andr"])));
        print("成功插入第" + str(index) + "行")
        index += 1;
    # 提交
    db.commit()
    cur.close()
    db.close()


def main():
    fromJsonToMysql("skin-tones-emojis-v13.0.json", table="skin_tones_emojis")


if __name__ == "__main__":
    main()
