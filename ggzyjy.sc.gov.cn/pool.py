from pathos.multiprocessing import Pool


def pool(data, cb, processNumn=10):
    try:
        Len = len(data)
        print("一共" + str(Len) + "个数据")
        print("开始爬取....")
        p = Pool(processNumn)
        args = []
        c = 0
        for item in data:
            args.append((item['linkurl'], c))
            c += 1
        ret = p.starmap(cb, args)
        print("成功爬取所有数据")
        return ret
    except Exception as e:
        print(e)
