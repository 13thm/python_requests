import requests
import  re
from lxml import html


class pachou():
    pass
    def  __init__(self):
        self.url="https://www.ip138.com/mobile.asp?mobile=18323416055&action=mobile"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }
        self.data={'mobile': '18323416055','action': 'mobile'}
    def get(self):
        try:
            r=requests.post(self.url,headers=self.headers,data=self.data)
            r.encoding="UTF-8"
            r.raise_for_status()
            return r.content.decode()
        except:
            print("这里出错了哦!")
            return ""


    def run(self):
        text=self.get()
        print(text)



if __name__ == '__main__':
    s=pachou()
    s.run()