u = "./skin-tones-emojis-v13.0.html"
jsonName = u.split(".html")[0]+".json"
try:
    file = open(jsonName, mode='w', encoding="utf8")
except Exception:
    print("Error can't open")
else:
    file.write("1231")
    file.flush()
    file.close()
    print('数据写入文件' + jsonName)