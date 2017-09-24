from collections import MutableMapping
import re
import logging

logger = logging.getLogger(__name__)


def romanToInt(s):
    sum = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(s) - 1):
        if convert[s[i]] < convert[s[i + 1]]:
            sum = sum - convert[s[i]]
        else:
            sum = sum + convert[s[i]]
    return sum + convert[s[-1]]


class Schedule(MutableMapping):
    def __init__(self):
        self.store = {}

    def _parse(self, title):
        number = 0
        if title.find('（'):
            if title.find('Part') > -1:
                number = re.findall(r"Part(.*?)）", title)
                if number:
                    number = number[0].strip()
                    if number.isdigit():
                        number = int(number)
                    else:
                        number = romanToInt(number)
                else:
                    number = 0
            elif title.find('P') > -1:
                number = re.findall("（P(.*?)）", title)
                if number:
                    number = number[0].strip()
                    if number.isdigit():
                        number = int(number)
                    else:
                        number = 0
                else:
                    number = 0
            elif title.find('完'):
                number = 100
            elif title.find('上'):
                number = 0
            elif title.find('中'):
                number = 1
            elif title.find('下'):
                number = 2
        else:
            number = 0
        subhead = title
        logger.info("number, subhead {} {}".format(number, subhead))
        return number, subhead

    def __getitem__(self, key):
        values = []
        for k, v in self.store.items():
            if key in k:
                values.append(v)
        return values

    def __setitem__(self, key, value):
        title, url, play = value
        number, subhead = self._parse(title)
        get_key = (key, number)
        get_value = (play, subhead, url)
        logger.info("{} {}".format(get_key, get_value))
        self.store[get_key] = get_value

    def _schedule_to_show(self, store):
        schedule = {}
        for k, v in store.items():
            name, number = k
            play, subhead, url = v
            if name in schedule.keys():
                item = schedule[name]
                exit_hots, value = item
                play = exit_hots + play
                value.append((number, subhead, url))
                schedule[name] = (play, value)
            else:
                schedule[name] = (play, [(number, subhead, url)])
        show_list = [(k, v[0], v[1]) for k, v in schedule.items()]
        show_list.sort(key=lambda x: x[1], reverse=True)
        return show_list

    def __str__(self):
        show_list = self._schedule_to_show(self.store)
        store = []
        for k, v, sub_list in show_list:
            store.append(k + ':')
            sub_list.sort()
            for s, subhead, url in sub_list:
                # store.append("    " + subhead)
                store.append("    " + url)
        return "\n\r".join(store)

    def __delitem__(self, key):
        items = list(self.store.items())
        for k, v in items:
            if key in k:
                del self.store[k]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
