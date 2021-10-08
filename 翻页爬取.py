import requests
from lxml import html
import pandas as pd
etree=html.etree

class page_sprider():
    def __init__(self):
        self.str_url="https://www.ryjiaoyu.com/tag/details/7"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    def get_html(self,str_url):
        try:
            r=requests.get(str_url,headers=self.headers)
            r.raise_for_status()
            r.encoding="utf-8"
            return r.content.decode()
            r.raise_for_status()
            r.encoding="utf-8"
        except:
            print("获取网页失败!")
            return ""
    def display(self,html):
        text=etree.HTML(html)
        #分组
        li_list=text.xpath('//ul[@class="block-items"]/li[@class="block-item"]')
        data_list=[]
        for li in li_list:
            lie=[]
            book_name=li.xpath('.//h4[@class="name"]/a/@title')
            lie.append(book_name[0])
            book_price=li.xpath('.//div[@class="book-info"]//span[@class="paperback"]/span/text()')
            lie.append(book_price[0])
            book_url=li.xpath('.//h4[@class="name"]/a/@href')
            lie.append("https://www.ryjiaoyu.com/"+book_url[0])
            book_author=li.xpath('.//div[@class="book-info"]//div[@class="author"]/span/text()')
            lie.append(book_author[0])
            data_list.append(lie)
        return data_list
    def save(self,data):
        df=pd.DataFrame(data,columns=["书名","价格","url","作者"])
        df.set_index("书名",inplace=True)
        path=r"./picture/1.csv"
        df.to_csv(path,encoding="gbk",mode="a")



    def run(self):
        #实现主要逻辑
        for i in range(35):
            str_html=self.get_html(self.str_url+"?page="+str(i))
            data=self.display(str_html)
            self.save(data)


if __name__ == '__main__':
    sprider=page_sprider()
    sprider.run()