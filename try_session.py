import requests


class Renren():
    def __init__(self,account,password):
        self.star_url="https://passport.zhihuishu.com/login"
        self.heards={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        self.data={"account": account,"password": password}

    def get_session(self):
        session=requests.session()
        s=session.post(self.star_url,headers=self.heards,data=self.data)
        s.encoding="utf-8"
        s.raise_for_status()
        url1="https://www.zhihuishu.com/"
        r=session.get(url=url1)
        return r.content.decode()

    def run(self): #实现主要逻辑
        text=self.get_session()
        print(text)


if __name__ == '__main__':
    account=input("请输入你的账户:")
    password=input("请输入你的密码:")
    spider=Renren(account,password)
    spider.run()