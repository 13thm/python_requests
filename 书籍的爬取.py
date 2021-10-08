import requests
from lxml import html
import pandas as pd
etree=html.etree


class Book_Spider():
    def __init__(self):
        self.str_url="https://www.ryjiaoyu.com/"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    def get_html(self):
        try:
            r=requests.get(self.str_url,headers=self.headers)
            r.raise_for_status()
            r.encoding="UTF-8"
            return r.content.decode()
        except:
            print("网页获取:出现错误!")
            return ""

    def display(self,content):
        text=etree.HTML(content)
        # 用xpath 分组获取信息
        li_list=text.xpath('//*[@id="block-102"]//li[@class="block-item"]')
        all_datas=[]
        for li in li_list:
            data_list=[]
            book_name=li.xpath('./div[@class="book-info"]//h4[@class="name"]/a/@title')
            data_list.append(book_name[0] if len(book_name)>0 else None)
            book_data=li.xpath('./div[@class="book-info"]//p[@class="intro"]/text()')
            data_list.append(book_data[0] if len(book_data)>0 else None)
            book_author=li.xpath('./div[@class="book-info"]//div[@class="author"]/span/text()')
            # book_author=[book_author.strip()]
            data_list.append(book_author[0] if len(book_author)>0 else None)
            book_price = li.xpath('.//span[@class="paperback"]/span[@class="price"]/text()')
            data_list.append(book_price[0] if len(book_price)>0 else None)
            all_datas.append(data_list)

        return all_datas

    def save(self,datas):
        print(datas)
        df=pd.DataFrame(datas,columns=["书名","书介绍","作者","价格"])
        path=r'./picture/书籍信息.xlsx'
        df.to_excel(path)





    def run(self): #实现主要逻辑
        content=self.get_html()
        datas=self.display(content)
        self.save(datas)




if __name__ == '__main__':
    sprider=Book_Spider()
    sprider.run()