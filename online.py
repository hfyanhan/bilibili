
import requests
import os
import time

a=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())

decdw=1        
while decdw<=24 :
    a=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
    
    url = "https://api.bilibili.com/x/web-interface/online"
    req = requests.get(url)
    text = req.text
    filename = "online.txt"
    f=open(filename, "a", encoding='utf-8')
    f.write(a)
    f.write("\n")
    f.write(text)
    f.write("\n")
    f.close()
    decdw=decdw+1
    time.sleep(600)