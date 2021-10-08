import requests
from lxml import html
# etree=html.etree
# url="http://www.kekenet.com/cet4/f/fyzt/"
# headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# r=requests.get(url,headers=headers)
# r.raise_for_status()
# r.encoding="uft-8"
# text=etree.HTML(r.text)
# li_list=text.xpath('//ul[@id="menu-list"]/li')
# url_list=[]
# for li in li_list:
#     ul=li.xpath('.//h2/a/@href')
#     url_list.append(ul)
# for u in url_list:
#     print(u)
#     x=requests.get(u,headers=headers)
#     x.encoding='utf-8'
#     page=etree.HTML(x.text)
#     content=page.xpath('//span[@style="white-space:normal]/text()')
#     with open(r'C:\Users\三水~~~\Desktop\英语翻译.txt','a+',encoding="utf-8") as f:
#         f.write(content+"\n")
