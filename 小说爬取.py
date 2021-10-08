import requests
from lxml import html
import pandas as pd
etree=html.etree

class XS_sprider():
    def __init__(self):
        self.str_url="https://www.qidian.com/rank/fengyun?style=1&"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}


    def get_html(self,url):
        try:
            r=requests.get(url=url,headers=self.headers)
            r.raise_for_status()
            r.encoding="UTF-8"
            return r.content.decode()
        except:
            print("网页获取失败")
            return ""
    def display_html(self,html):
        text=etree.HTML(html)
        li_list=text.xpath('//div[@class="main-content-wrap fl"]//div[@id="rank-view-list"]//div[@class="book-img-text"]/ul/li')
        list_books=[]
        for li in li_list:
            list_book = []
            book_name=li.xpath('.//div[@class="book-mid-info"]/h4/a/text()')
            list_book.append(book_name[0])
            book_athor=li.xpath('.//p[@class="author"]//a[@class="name"]/text()')
            list_book.append(book_athor[0])
            book_data=li.xpath('.//p[@class="intro"]//text()')
            print(book_data[0].strip())
            list_book.append(book_data[0].strip())
            book_date=li.xpath('.//p[@class="update"]//span/text()')
            list_book.append(book_date)
            list_books.append(list_book)
        return list_books

    def save(self,list_books):
        df=pd.DataFrame(list_books,columns=None,index=None)
        path=r'./picture/小说.csv'
        df.to_csv(path,encoding="gbk",mode="a")

    def run(self):
        for i in range(1,6):
            url=self.str_url+"page=".format(i)
            html_content=self.get_html(url)
            list_books=self.display_html(html_content)
            self.save(list_books)


if __name__ == '__main__':
    spider=XS_sprider()
    spider.run()