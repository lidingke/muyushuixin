import pickle
import re
import requests
from config import  URL_EACH_AV, URL_PATTERN, PAGES


# def get_session():
#     ses = requests.Session()
#     ses.cookies.update(COOKIES_DICT)
#     ses.headers.update(HEAD)
#     return ses

#error code '{"status":true,"data":{"tlist":null,"vlist":null,"count":493,"pages":17}}'
from schedule import Schedule


def get_responses():
    urls = {URL_PATTERN.format(page = p+1) for p in range(PAGES)}
    datas = []
    for url in urls:
        print(url)
        data = requests.get(url).json()
        datas.append(data)

    with open("datas.pickle","wb") as f:
        f.write(pickle.dumps(datas))


def parse(response):
    data = response['data']
    vlist = data['vlist']
    items = []
    for v in vlist:
        title = v['title']
        if title.find('木鱼微剧场')>0:
            key = re.findall('《(.*?)》', title)
            if key:
                key = key[0]
            else:
                raise ValueError('none re key in title')
            url = URL_EACH_AV.format(aid = v['aid'])
            item = (key,(title,url,v['play'],))
            # print(item)
            items.append(item)
    return items

def parse_data():
    with open("datas.pickle", 'rb') as f:
        picks = pickle.load(f)
    items = []
    for p in picks:
        items.extend(parse(p))
    schedule = Schedule()
    for k,v in items:
        schedule[k]=v
    print(schedule)
    print(len(schedule))


if __name__ == '__main__':
    get_responses()
    parse_data()
