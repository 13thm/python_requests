import requests
from queue import Queue
import threading
from lxml import html
from urllib import request
etree=html.etree
# 注意一下 while Ture 要在 run 方法里面执行!

class Producer(threading.Thread):
    def __init__(self,url_queue,img_queue,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.url_queue=url_queue
        self.img_queue=img_queue
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    def get_urls(self):
        for x in range(3):
            url="https://818ps.com/muban/keaidebiaoqingbao/{}.html".format(x)
            self.url_queue.put(url)
            print("网址进队url_queue")
    def paser_html(self):
        url=self.url_queue.get()
        print("网址出队!")
        r=requests.get(url,headers=self.headers)
        r.encoding="utf-8"
        text=etree.HTML(r.content.decode())
        imgs=text.xpath('//div[@id="masonry"]//div[@class="min-img"]/img')
        for x in imgs:
            img="http:"+x.get("img-original")
            name=x.get("title")
            self.img_queue.put([img,name])
            print("照片网址入队")

    def run(self):
        self.get_urls()
        while True:
            print(self.url_queue.qsize())
            if (self.url_queue.empty()):
                print("完咯1")
                break
            self.paser_html()


class Comsumer(threading.Thread):
    def __init__(self,url_queue,img_queue,*args,**kwargs):
        super(Comsumer,self).__init__(*args,**kwargs)
        self.url_queue=url_queue
        self.img_queue=img_queue
    def run(self):
        while True:
            print(self.url_queue.qsize(),self.img_queue.qsize())
            if(self.url_queue.empty() and self.img_queue.empty()):
                print("完咯2")
                break
            img_url=self.img_queue.get()
            path=r"./img/{}.png".format(img_url[1])
            request.urlretrieve(img_url[0],path)
            print("照片出队")


def main():
    url_queue=Queue(10)
    img_queue=Queue(500)
    for i in range(3):
        t1=Producer(url_queue,img_queue)
        t1.start()
    for i in range(6):
        t2=Comsumer(url_queue,img_queue)
        t2.start()

if __name__ == '__main__':
    main()