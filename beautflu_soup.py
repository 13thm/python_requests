from bs4 import BeautifulSoup
import requests

class school_spider():
    def __init__(self):
        self.url="http://www.cqie.edu.cn/html/2/mtjj/"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    def get_html(self):
        try:
            r=requests.get(self.url,headers=self.headers)
            r.encoding='gbk'
            r.raise_for_status()
            return r.text
        except:
            print("获取网页失败")
            return ""

    def get_datas(self,contents):
        soup=BeautifulSoup(contents,'html.parser')
        for row in soup.select('.nav_top cen clearfix'):
            print(row)


    def run(self):#实现主要逻辑
        contents=self.get_html()
        self.get_datas(contents)


if __name__ == '__main__':
    spider=school_spider()
    spider.run()
