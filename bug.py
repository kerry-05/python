import requests
from bs4 import BeautifulSoup


def test():
    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")  # 將網頁資料GET下來
    soup = BeautifulSoup(r.text, "html.parser")  # 將網頁資料以html.parser
    sel = soup.select("div.title a")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    ahq = soup.select("head.title")
    for s in sel:
        print(s["href"], s.text)



