#作者：肥肥杨
#链接：https://www.zhihu.com/question/56924570/answer/236892766
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
import re
import os
from json import loads
import time

import funcbili
# B站API详情 https://github.com/Vespa314/bilibili-api/blob/master/api.md

# 视频AV号列表
aid_list = []

a=time.strftime("%Y-%m-%d",time.localtime())+'p'

# 获取一个AV号视频下所有评论
def getAllCommentList(item):
    url = "http://api.bilibili.com/x/reply?type=1&oid=" + str(item) + "&pn=1&nohot=1&sort=0"
    r = requests.get(url)
    numtext = r.text
    json_text = loads(numtext)
    commentsNum = json_text["data"]["page"]["count"]
    page = commentsNum // 20 + 1
    for n in range(1,page):
        url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn="+str(n)+"&type=1&oid="+str(item)+"&sort=1&nohot=1"
        text = submit(url,2)
        filename = './'+a+'/'+str(item) + ".txt"
        f=open(filename, "a", encoding='utf-8')
        f.write(text)
        print("文件写入中")

def main():
    try:
        os.mkdir(a)
    except Exception:
        print('Error')
    f=open('need3.txt',mode='r',encoding='utf-8')
    aid_list=realine(f)
    for item in aid_list:
        getAllCommentList(item)