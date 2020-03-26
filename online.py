
#作者：肥肥杨
#链接：https://www.zhihu.com/question/56924570/answer/236892766
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
#import re
import os
#import sys
#from json import loads
import time
# B站API详情 https://github.com/Vespa314/bilibili-api/blob/master/api.md

# 视频AV号列表
aid_list = []

a=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())

# 评论用户及其信息
info_list = []


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

    # 爬取逆风笑 只爬取第一页的第一个
    #getAllAVList(2019740,1,1)
decdw=1        
        #saveTxt(item,info_list)
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