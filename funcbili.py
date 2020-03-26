def isexist(s):
    try:
        f=open(s,mode="r",encoding="gb2312")
    except IOError:
       return 0
    f.close()
    return 1
def submit(htm,sleept):
    import requests,time
    while 1:
        der=0
        try:
            r=requests.get(htm)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
        except:
            print("获取Url失败,继续尝试")
            time.sleep(sleept)
            der=3
        if der==0 :
            break
    w=r.text
    return w

def wrhtml(text,num,how,hou):#将查询到的网页写入文件
    num=str(num)
    num=num+"."+hou
    if how==2:
        f=open(num,mode="r",encoding="utf-8")
        q=f.read()
        return q
    f=open(num,mode="w",encoding="utf-8")
    f.write(text)
    f.close()
    return "Successfully!"
def realine(f):
    w=[]
    while 1:
        date=f.readline()
        if not date:
            break
        w.append(date[0:len(date)-1])
    print(w)
    return w