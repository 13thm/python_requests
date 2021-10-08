import  requests
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
r=requests.get("http://www.cqie.edu.cn/html/2/mtjj/",headers=headers)
r.encoding="gbk"
print(r.text)
# with open("./picture/唐浩淼.html","w") as f:
#     f.write(text)
