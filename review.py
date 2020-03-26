#作者：肥肥杨
#链接：https://www.zhihu.com/question/56924570/answer/236892766
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
import re
import os
#import sys
from json import loads
import time
# B站API详情 https://github.com/Vespa314/bilibili-api/blob/master/api.md

# 视频AV号列表
aid_list = []

a=time.strftime("%Y-%m-%d",time.localtime())+'p'

# 评论用户及其信息
info_list = []

# 获取指定UP的所有视频的AV号 mid:用户编号 size:单次拉取数目 page:页数
#def getAllAVList(mid, size, page):
    # 获取UP主视频列表
    #for n in range(1,page+1):
        #url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" + \
            #str(mid) + "&pagesize=" + str(size) + "&page=" + str(n)
        #r = requests.get(url)
       # text = r.text
        #json_text = loads(text)
        # 遍历JSON格式信息，获取视频aid
        #for item in json_text["data"]["vlist"]:
          #  aid_list.append(item["aid"])
    #print(aid_list)

# 获取一个AV号视频下所有评论
def getAllCommentList(item):
    url = "http://api.bilibili.com/x/reply?type=1&oid=" + str(item) + "&pn=1&nohot=1&sort=0"
    r = requests.get(url)
    numtext = r.text
    json_text = loads(numtext)
    commentsNum = json_text["data"]["page"]["count"]
    page = commentsNum // 20 + 1
    for n in range(1,page):
        while 1:
            try:
                flag=0
                url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn="+str(n)+"&type=1&oid="+str(item)+"&sort=1&nohot=1"
                req = requests.get(url)
            except Exception:
                time.sleep(2)
                flag=1
            if flag==0:
                break;
        text = req.text
        filename = './'+a+'/'+str(item) + ".txt"
        f=open(filename, "a", encoding='utf-8')
        f.write(text)
        print("文件写入中")
        #json_text_list = json.loads(text)
        #for i in json_text_list["data"]["replies"]:
            #info_list.append([i["member"]["uname"],i["content"]["message"]])
    # print(info_list)

# 保存评论文件为txt
#def saveTxt(filename,filecontent):
    #filename = './'+a+'/'+str(filename) + ".txt"
    #for content in filecontent:
        #with open(filename, "a", encoding='utf-8') as txt:
            #txt.write(content[0] +' '+content[1].replace('\n','') + '\n\n')
        #print("文件写入中")

def main():
    # 爬取逆风笑 只爬取第一页的第一个
    #getAllAVList(2019740,1,1)
    
    try:
        os.mkdir(a)
    except Exception:
        print('Error')
    f=open('need3.txt',mode='r',encoding='utf-8')
    while 1:
        date=f.readline()
        if not date:
            break
        aid_list.append(date[0:len(date)-1])
    for item in aid_list:
        info_list.clear()
        qw=getAllCommentList(item)
        
        #saveTxt(item,info_list)