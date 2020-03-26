import requests
import time
decwww=1
decw=1
while decwww<=4:
    while decw<=12:
        a=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        r=requests.get('https://www.bilibili.com/video/online.html')
        se=r.text
        filn=a+"-online.html"
        f=open(filn,mode="w",encoding="utf-8")
        f.write(se)
        f.close()
        time.sleep(1200)
        decw=decw+1
    decwww=decwww+1