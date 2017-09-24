import pickle

from requester import parse
from schedule import Schedule
import logging
SCHEDULE_DATAS = [
]

def test_schedule():
    s = Schedule()


def test_get_from_url():
    # logging.basicConfig(level=logging.INFO)
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
    test_get_from_url()