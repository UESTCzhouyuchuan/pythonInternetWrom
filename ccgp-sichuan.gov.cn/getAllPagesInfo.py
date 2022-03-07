from multiprocessing import Pool

from bs4 import BeautifulSoup
from requests import get

from _file import *


def pool(data, cb, key, processNumn=10):
    try:
        Len = len(data)
        print("一共" + str(Len) + "个数据")
        print("开始爬取....")
        p = Pool(processNumn)
        args = []
        c = 0
        for item in data:
            args.append((item, key, c))
            c += 1
        ret = p.starmap(cb, args)
        print("成功爬取所有数据")
        return ret
    except Exception as e:
        print(e)


def getAttachment(bs, key, title):
    urlPrefix = "http://www.ccgp-sichuan.gov.cn/"
    attachment = []
    attach = bs.find_all('a', string="附件")
    if attach is not None:
        c = 1
        for item in attach:
            url_end = item['href']
            # 错误处理
            # if url_end == urlPrefix or url_end == "//" or len(url_end) <= 2:
            #     continue
            if url_end.startswith('http'):
                fn_url = url_end
            else:
                fn_url = urlPrefix + item['href']
            attachment.append(fn_url)
            # end = fn_url.split('.')[-1]
            # files_end = ['rar', 'pdf', 'zip', 'doc', 'docx']
            # new_filename = re.sub(r'[\\/:*?"<>|\r\n]+', "_", title)
            # try:
            #     with get(fn_url) as resp:
            #         if end.lower() not in files_end:
            #             content_disposition = resp.headers['Content-disposition']
            #             if content_disposition is not None:
            #                 end = content_disposition.split('.')[-1]
            #                 if end[-1] == '"' or end[-1] == "'":
            #                     end = end[0:-1]
            #         fn = f'./files/{key}/{new_filename}_附件{c}.{end}'
            #         try:
            #             with open(fn, 'wb') as f:
            #                 f.write(resp.content)
            #                 f.close()
            #                 print(f'保存{fn}成功')
            #         except Exception as e:
            #             print(f'保存文件失败, {fn_url}, {fn},{e}')
            #         resp.close()
            # except Exception as e:
            #     print(f'下载附件失败, {fn_url},{e}')
            # else:
            #     attachment.append(fn_url)
            #     c += 1
    return attachment


def Page1(urlEnd, key, index):
    urlPrefix = "http://www.ccgp-sichuan.gov.cn"
    if urlEnd.lower().startswith('http'):
        url = urlEnd
    else:
        url = urlPrefix + urlEnd
    if index is not None:
        tip = f'第{index + 1}条数据, {url}: '
    else:
        tip = f"修补数据,{url}： "
    try:
        ret = {}
        res = get(url)
        bs = BeautifulSoup(res.content, features="html.parser", from_encoding="UTF-8")
        res.close()
        cont_info = bs.find(class_="cont-info")
        title = cont_info.find('h1', recursive=False).string
        time_ = cont_info.find('p', class_='time', recursive=False).string
        title = ILLEGAL_CHARACTERS(title)
        time_ = ILLEGAL_CHARACTERS(time_)
        ret['title'] = title
        ret['time'] = time_.replace('系统发布时间：', '')
        if cont_info.find(id="myPrintArea") is None:
            my_print_area = cont_info.find('p', class_='time').find_next('p').get_text()
        else:
            my_print_area = cont_info.find(id="myPrintArea").get_text()
        my_print_area = ILLEGAL_CHARACTERS(my_print_area)
        ret['myPrintArea'] = my_print_area
        attachment = getAttachment(cont_info, key, title)
        ret['attachment'] = attachment
        print(f'{tip} 爬取成功')
    except Exception as e:
        print(f'获取页面失败, {url}, {e}')
    else:
        ret['type'] = 1
        ret['url'] = url
        return ret


def Page2(url, key, index):
    if index is not None:
        tip = f'第{index + 1}条数据, {url}: '
    else:
        tip = f"修补数据,{url}： "

    try:
        ret = {}
        res = get(url)
        bs = BeautifulSoup(res.content, features="html.parser", from_encoding="UTF-8")
        res.close()
        con_body = bs.find(class_="conBody")
        title = con_body.find('h1').string
        title = ILLEGAL_CHARACTERS(title)
        project_number = con_body.find(class_="project-number").get_text()
        project_number = ILLEGAL_CHARACTERS(project_number)
        lines = bs.find(id="lines").get_text()

        lines = ILLEGAL_CHARACTERS(lines)

        ret['title'] = title
        ret['project_number'] = project_number
        ret['content'] = lines
        # print(ret)
        print(f'{tip} 爬取成功')
    except Exception as e:
        print(f'获取页面失败, {url}, {e}')
    else:
        ret['type'] = 2
        ret['url'] = url
        return ret


def Page3(urlEnd, key, index):
    urlPrefix = "http://www.ccgp-sichuan.gov.cn"
    if urlEnd.lower().startswith('http'):
        url = urlEnd
    else:
        url = urlPrefix + urlEnd
    if index is not None:
        tip = f'第{index + 1}条数据, {url}: '
    else:
        tip = f"修补数据,{url}： "
    try:
        ret = {}
        res = get(url)
        bs = BeautifulSoup(res.content, features="html.parser", from_encoding="UTF-8")
        res.close()
        my_print_area = bs.find(id="myPrintArea")
        my_print_area_text = ILLEGAL_CHARACTERS(my_print_area.get_text())
        ret['myPrintArea'] = my_print_area_text
        report_title = my_print_area.find(class_="reportTitle", recursive=False)
        title = report_title.find('h1', recursive=False).string
        time_ = report_title.find('span', recursive=False).string
        title = ILLEGAL_CHARACTERS(title)
        time_ = ILLEGAL_CHARACTERS(time_)
        ret['title'] = title
        ret['time'] = time_.replace('系统发布时间：', '')
        attachment = getAttachment(bs, key, title)
        ret['attachment'] = attachment
        print(f'{tip} 爬取成功')
    except Exception as e:
        print(f'获取页面失败, {url}, {e}')
    else:
        ret['type'] = 3
        ret['url'] = url
        return ret


def getSinglePageInfo(urlEnd, key, index=None):
    if urlEnd.startswith('http://202.61.88.152:9004'):
        ret = Page2(urlEnd, key, index)
    elif urlEnd.startswith('/view/staticpags/qt'):
        ret = Page3(urlEnd, key, index)
    else:
        ret = Page1(urlEnd, key, index)

    return ret


def getAllPagesInfo(key, processNum = 10):
    dic = "./files/" + key
    data = readFromFile(dic + '/url.json')
    result = pool(data, getSinglePageInfo, key, processNum)
    writeToFile(dic + '/result.json', result)


if __name__ == '__main__':
    getAllPagesInfo("地质灾害")
    # ret = getSinglePageInfo('/view/staticpags/qt/402886876285b3eb01628acfd46a0e5f.html', '地质灾害')
    # print(ret)
