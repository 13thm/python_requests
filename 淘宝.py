import  requests
import re
def get_html(url,time=10):
    head = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/89.0.4389.82 Safari/537.36"
    } #设置用户代理，应对简单反爬虫
    try:
        r = requests.get(url,headers=head, timeout=time)  # 发送请求
        r.encoding = r.apparent_encoding  # 设置返回内容的字符集编码
        r.raise_for_status()  # 返回的状态码不等于200抛出异常
        return r.text  # 返回网页的文本内容
    except Exception as error:
      print(error)
def getdata(t):
    s="德国佳仁电动新款按摩椅全自动家用小型太空"
    if(s in t):
        print("在里面")
    else:
        print("不在")


if __name__=="__main__":
    # url="https://www.taobao.com/"
    url="https://editor.588ku.com/muban/zhongqing.html"
    print(get_html(url))
    t=get_html(url)
    getdata(t)