import requests
import json
w=[]
f=open('a2b-input.txt',mode='r',encoding='utf-8')
while 1:
    date=f.readline()
    if not date:
        break
    w.append(date[0:len(date)-1])
aid_list=[]
for av in w:
    url="https://api.bilibili.com/x/web-interface/view?aid="+str(av)
    eww=requests.get(url).text
    json_text = json.loads(eww)
    print(json_text)
    aid_list.append(json_text["data"]['bvid'])
f=open("a2b-output.txt", "w", encoding="utf-8")
for i in aid_list:
    qqq=str(i)+'\n'
    f.write(qqq)
f.close()