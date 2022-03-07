# 四川省公共资源交易信息网

## 介绍

### main.py
主函数，通过设置 `key`更改搜索的关键字
```python
def main():
    # 关键字
    key = "监测预警" #修改这里

    # 获得url,自动写入文件
    getAllUrl(key)

    # 获得全部url中的数据，并写入文件中
    getAllPagesInfoToJson(key, 25)
    # 写入xlsx中
    JsonToXlsx(key)
```
### 使用python进程池的注意点
如果电脑cpu性能较差，适当降低设置的进程数量
通过设置

```python
def main():
    # 关键字
    key = "监测预警"

    # 获得url,自动写入文件
    getAllUrl(key)

    # 获得全部url中的数据，并写入文件中
    getAllPagesInfoToJson(key, 25) # 修改这里的第二个参数
    # 写入xlsx中
    JsonToXlsx(key)
```