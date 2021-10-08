from bs4 import BeautifulSoup
import pymysql
import requests

class News_Spider():
    def __init__(self):
        self.start_url="http://www.ccgp-shaanxi.gov.cn/"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

    def requst_url(self):
        try:
            r=requests.get(self.start_url,headers=self.headers)
            r.encoding="utf-8"
            r.raise_for_status()
            return r.content.decode()
        except:
            print("请求网页出现错误!")
            return ""

    def get_datas(self,html):
        all_data=[]
        soup=BeautifulSoup(html,"html.parser")
        # soup=soup.find_all(attrs={"id":"MessageNote"})
        list_a=soup.select('#MessageNote a')
        for a in list_a:
            data=[]
            data.append(a.text.strip())
            data.append(a.attrs["href"])
            all_data.append(data)
        return all_data

    def sava(self,datas):
        db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="myspider",
                             charset="utf8")
        cs1 = db.cursor()
        for i in datas:
            sql = "INSERT INTO news(名字,url)  values ('%s','%s')" \
                  % (str(i[0]),str(i[1]))
            try:
                cs1.execute(sql)
                db.commit()
            except:
                print("插入失败")
                db.rollback()
        cs1.close()
        db.close()

    def run(self):
        html=self.requst_url()
        datas=self.get_datas(html)
        self.sava(datas)

if __name__ == '__main__':
    news=News_Spider()
    news.run()