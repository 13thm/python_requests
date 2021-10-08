import requests
from bs4 import BeautifulSoup
import re
from lxml import html
import pandas as pd
# str="""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <div class="nihao">
#     <div>
#     <p str= "aaa">
#     <a>16165</a>
#     </p>
#     </div>
#     <div>
#     <p str="bbbb">
#     <a>sdad</a>
#     </p>
#     </div>
#     <div>
#     <p str="cccc">
#     <a></a>
#     </p>
#     </div>
#     <div>
#     <p str="ggggg">
#     <a>sdqwqe</a>
#     </p>
#     </div>
# </div>
# </body>
# </html>
#
#
# """
# etree=html.etree
# html1=etree.HTML(str)
# path=html1.xpath('//div[@class="nihao"]/div')
# print(path)
# for i in path:
#     print(i.xpath(".//a/text()"))
# li=[[1,2],[2,4]]
#
# df=pd.DataFrame(li,columns=["第一","第二"])
# print(df)