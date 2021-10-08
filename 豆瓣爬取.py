import  requests
from lxml import html
import pymysql
etree=html.etree

class Dan_spider():
    def __init__(self):
        self.url="https://book.douban.com/latest?icn=index-latestbook-all"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    def get_html(self):
        try:
            r=requests.get(self.url,headers=self.headers)
            r.encoding="utf-8"
            r.raise_for_status()
            return r.content.decode()
        except:
            print("获取网页失败")
            return ""
    def display(self,book_html):
        text=etree.HTML(book_html)
        list_li=text.xpath('//div[@id="wrapper"]//div[@class="article"]//ul[@class="cover-col-4 clearfix"]/li')
        list_li+=text.xpath('//div[@id="wrapper"]//div[@class="aside"]//ul[@class="cover-col-4 clearfix"]/li')
        db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="myspider",
                             charset="utf8")
        cs1 = db.cursor()
        for li in list_li:
            book_name=li.xpath('.//div[@class="detail-frame"]/h2/a/text()')[0]
            book_fen=li.xpath('.//div[@class="detail-frame"]//span[@class="font-small  color-lightgray"]/text()')[0]
            books=li.xpath('.//div[@class="detail-frame"]//p[@class="color-gray"]/text()')[0]
            book_list=books.strip().split("/")
            book_author,book_c,book_time=book_list[0],book_list[1],book_list[2]
            book_data=li.xpath('.//div[@class="detail-frame"]//p[@class="detail"]/text()')[0]
            sql="INSERT INTO douban(书名,评分,作者,出版社,出版时间,图书介绍)  values ('%s','%s','%s','%s','%s','%s')"\
                %(book_name,book_fen,book_author,book_c,book_time,book_data)
            try:
                cs1.execute(sql) # 执行SQL语句
                db.commit() #提交到数据库执行
            except:
                print("插入失败")
                db.rollback() # 这个是让他数据回滚,相当什么都没有发生过
        cs1.close()
        db.close()
    def run(self):
        # 实现主要逻辑
        book_html=self.get_html()
        self.display(book_html)


if __name__ == '__main__':
    s=Dan_spider()
    s.run()