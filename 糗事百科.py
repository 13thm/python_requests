import requests
from lxml import html
etree=html.etree

class qiushi():
    def __init__(self):
        self.star_url='https://www.qiushibaike.com/text/'
        self.headers={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

    def response(self,star_url):
        try:
            r=requests.get(star_url)
            r.raise_for_status()
            r.encoding='utf-8'
            return r.content.decode()
        except:
            print("请求网站出错了")
            return ""

    def examine(self,str_html,all_list):
        html=etree.HTML(str_html)
        # 分组
        div_list=html.xpath('//div[@class="col1 old-style-col1"]/div[@class="article block untagged mb15 typs_hot"]')
        for div in div_list:
            dict_div={}
            # print(div.xpath('./div//a[@rel="nofollow"]/img/@src'))
            picture=div.xpath('./div//a[@rel="nofollow"]/img/@src')
            name=div.xpath('./div//a[@rel="nofollow"]/img/@alt')
            text=div.xpath('./a//div[@class="content"]/span/text()')
            dict_div["名字"]=name[0] if len(name)>0 else None
            dict_div["头像图片链接"]="https:"+ picture[0] if len(picture)>0 else None
            st=""
            for i in text:
                st=st+i
            dict_div["文本"]=st if len(st)>0 else None
            all_list.append(dict_div)
        print(all_list)
    def save(self,all_list):
        with open("./picture/糗事百科.txt",'a+',encoding="utf-8") as f:
            for dic in all_list:
                f.write(dic["名字"]+"\n"+dic["头像图片链接"]+"\n"+dic["文本"])
                f.write("*"*100+"\n")


    def fanye(self):
        pass




    def run(self):
        # 1./获取第一个网址
        all_list=[]
        str_html=self.response(self.star_url)
        self.examine(str_html,all_list)
        self.save(all_list)

        # 2.寻找到相应的信息
        # 3.保存数据!
        # 4.翻页,和重复!
        pass



if __name__ == '__main__':
    T=qiushi()
    T.run()