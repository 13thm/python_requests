import requests
import re

def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        # print(r.text)
        return r.text
    except:
        return ""

def getinformation(text,all_goods):
    try:
        price = re.findall('&yen;</b>(.*)</em>', text)
        name=re.findall('\" target=\"_blank\" title=(.*)data-p=',text)
        for i in range(len(price)):
            all_goods.append([price[i],name[i]])
        # print(all_goods)

    except:
        print(" ")

def printf(all_good):
    with open(r"天猫.txt","a+",encoding="UTF-8") as f:
        tplt = "{:4}\t{:8}\t{:16}"
        print(tplt.format("序号", "价格", "商品名称"))
        count = 0
        for g in all_goods:
            count = count + 1
            f.writelines(tplt.format(count, g[0], g[1])+"\n")
            print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    all_goods=[]
    url="https://list.tmall.com/search_product.htm?q=书包"
    text=gethtml(url)
    getinformation(text,all_goods)
    printf(all_goods)