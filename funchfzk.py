def listm(s,a):
    i=s
    w=[]
    while i<=a:
       num=i
       num=str(num)
       ser=num
       ser=ser+" %d5' #"
       sear={'num':num,
             'ser':ser}
       w.append(sear)
       i=i+1
    return w
def isexist(s):
    try:
        f=open(s,mode="r",encoding="gb2312")
    except IOError:
       return 0
    f.close()
    return 1
def submit(kh,htm):#将cookies附加到post请求
    import requests
    Cookie={'PHPSESSID':"fl45cnps1ovg813qqo8iob29g1"}    
    date={"find_fzkh":kh,"find_fzwh":"","seach_name":" 查  询 "}
    while 1:
        der=0
        try:
            r=requests.post(htm,data=date,cookies=Cookie)
        except Exception:
            print(1)
            der=3
        if der==0 :
            break
    w=r.text
    return w
def expect(num,how,f):#确定该考生是否需爬取
    while 1:
        t=f.readline()
        if not t :
            break;
        if int(t)==int(num) :
            f.close()
            return how
    f.close()
    return (how+1)%2
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
def tableq(kh,x,y,how,f):
    #f=open('qu.txt',mode='r',encoding='utf-8')
    w=[]
    while 1:
        date=f.readline()
        if not date:
            break
        date=date+' '
        length=len(date)
        i=0
        boon=""
        num=0
        
        sn=[]
        while i<length:
            if date[i]==' ':
                num=num+1
                sn.append(boon)
                #print(boon)
                if num==2:
                    w.append(sn)
                    sn=[]
                    num=0
                boon=""
                i=i+1
                continue
            if date[i]!='\n' :
                boon=boon+date[i]
            i=i+1
    if how==2 :
        return w
    if how==1 :
        kh=str(kh)[7:9]
    for a in w :
        if a[x]==kh :
            return a[y]
