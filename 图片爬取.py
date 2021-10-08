import requests
from bs4 import BeautifulSoup
import re


def getrequest(url,head):
    try:
        r = requests.get(url, headers=head, timeout=30)  # 发送请求
        r.encoding = "UTF-8" # 设置返回内容的字符集编码
        r.raise_for_status()  # 返回的状态码不等于200抛出异常
        # print(r.text)
        return r.text
    except:
        print("出错了!")
def save(text):
    soup=BeautifulSoup(text,"html.parser")
    text = soup.find_all(attrs={"class": "img-box"})
    # print(text)
    count=0
    for sr in text:
        ur=re.search(r'src=\"//(.*)\" t',str(sr))
        if ur is None :
            pass
        else:
            count+=1
            yy="http://"+ur.group(1)
            geturl(yy,count,len(text))


def geturl(ur,count,long):
    head = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/89.0.4389.82 Safari/537.36"
    }
    try:
        r=requests.get(ur,head)
        r.encoding="UTF-8"
        r.raise_for_status()
        with open(r"./picture/"+str(count)+".png","wb") as f:
            f.write(r.content)
        print("已经完成了{}%".format(int(count/long*100)))
    except:
        print("geturl出错了!")
if __name__ == '__main__':
    url="https://editor.588ku.com/muban/zhongqing.html"
    head={
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/89.0.4389.82 Safari/537.36"
    }
    text=getrequest(url,head)
    save(text)