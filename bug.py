def showbook(url,kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    try:
        pages = int(soup.select('.cnt_page span')[0].text)
        print("共有",pages,"頁")
        for page in range(1,pages+1):
            pageurl= url + '&page=' + str(page).strip()
            print("第",page,"頁",pageurl)
            showpage(pageurl,kind)

    except:showpage(url,kind)

def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    res = soup.find_all('div',{'class':'mod type02_m012 clearfix'})[0]
    items = res.select('.item')
    n = 0
    for item in items:
        msg = item.select('.msg')[0]
        src = item.select('a img')[0]["src"]
        title = msg.select('a')[0].text
        imgurl = src.split("?i=")[-1].split("&")[0]
        author = msg.select('a')[1].text
        publish = msg.select('a')[2].text
        date = msg.find('span').text.split(":")[-1]
        onsale = item.select('.price .set2')[0].text
        content = item.select('.txt_cont')[0].text.replace(" ","").strip

        print("\n分類:"+kind)
        print("書名:"+title)
        print("圖片網址:"+imgurl)
        print("作者:"+author)
        print("出版社:"+publish)
        print("出版日期:"+date)
        print(onsale)
        print("內容:"+content)
        n+=1
        print("n=",n)
            #if n==2: break#

def twobyte (kindno):
    if kindno<10:
        kindnostr = '0'+str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr

import requests
from bs4 import BeautifulSoup
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
list1=[]

kindno = 1
homeurl = 'https://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1'
mode = "?o=5&v=1"
url = "https://www.books.com.tw/web/books_nbtopm_"
html = requests.get(homeurl).text
soup = BeautifulSoup(html,'html.parser')
res = soup.find('div',{'class':'mod_b type02_l001-1 clearfix'})
hrefs = res.select("a")

for href in hrefs:
    kindurl = url + twobyte(kindno) +mode
    print("\nkindno=",kindno)
    kind =href.text
    showbook(kindurl,kind)
    kindno+=1

    listtitle = ["分類","書名","圖片網址","作者","出版社","出版日期","優惠價","內容"]
    sheet.append(listtitle)
    for item1 in  list1:
        sheet.append(item1)

workbook.save('books_all.xlsx')




