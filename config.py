PAGES = 17
# URL_PATTERN = "https://space.bilibili.com/927587#!/video?keyword=&order=pubdate&page={}&tid=0"
URL_PATTERN = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=927587&pagesize=30&tid=0&page={page}&keyword=&order=pubdate"
URL_EACH_AV = "https://www.bilibili.com/video/av{aid}/"
HEAD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", \
        "charset": "utf-8"}
