import requests
from lxml import etree
import pandas as pd

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.81 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def schools_get() -> list:
    schools = pd.read_excel('独立学院名单.xlsx').values
    schools = [''.join(i) for i in schools]
    return schools


def abb_get(school) -> str:
    url = 'https://baike.baidu.com/item/' + school
    res = requests.get(url, headers=headers)
    res1 = res.content.decode('utf-8')
    xpath = '//dl[@class="basicInfo-block basicInfo-left"]/dd[@class="basicInfo-item value"][2]/text()'
    html = etree.HTML(res1)
    a = html.xpath(xpath)[0]
    return a


def save(data):
    data.to_excel('全国高等学校中英文对应表3.xlsx', index=False)


def run():
    schools = schools_get()
    count = len(schools)
    out = []
    print(f'共{count}学校')
    for i in schools:
        index = schools.index(i) + 1
        print(f'已完成{index}/{count}')
        s = []
        try:
            a = abb_get(i)
        except:
            a = ''
        s.append(i)
        s.append(a)
        out.append(s)
    out = pd.DataFrame(out)
    save(out)


if __name__ == '__main__':
    run()
