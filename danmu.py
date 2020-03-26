#bilibili弹幕抓取
from funcbili import wrhtml,submit,realine
import requests
import re
import time
import os


we=time.strftime("%Y-%m-%d",time.localtime())+'d'

 
def parsePage(text,av):
    sffn=str(av)+".xml"
    try:
        print("解析文本...")
        keyStr = re.findall('"cid":[\d]*',text)#B站有两种寻址方式，第二种多一些
        if not keyStr:#若列表为空，则等于“False”
            keyStr = re.findall('cid=[\d]*', text)
            key = eval(keyStr[0].split('=')[1])
        else:
            key = eval(keyStr[0].split(':')[1])
        commentUrl = 'https://comment.bilibili.com/' + str(key) + '.xml'  # 弹幕存储地址
        print("再一次")
        commentText=we+'\n'+submit(commentUrl,0)
        s='./'+we+'/'+av
        wrhtml(commentText,s,1,"xml")
    except:
        print("解析失败")
        
def fordiff(ip):
    y=int(ip)
    if y==1:
        w=[]
        while 1:
            av =input('Put in bv number: ')  # 视频地址
            if av=='0':
                return w
            w.append(av)
    if y==2:
        f=open('need2.txt',mode='r',encoding='utf-8')
        return realine(f)
    if y==3:
        f=open('need5.txt',mode='r',encoding='utf-8')
        return realine(f)
        
def main(a):
    try:
        os.mkdir(we)
    except Exception:
        print(1)
    for bv in fordiff(a) :
        url="https://www.bilibili.com/video/"+str(bv)
        text=submit(url,0)
        parsePage(text,bv)
        print("Finish.")
#————————————————
#版权声明：本文为CSDN博主「某C姓工程师傅」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_41185456/article/details/79601563

#以上为原作者信息，本人在其基础上进行了修改。