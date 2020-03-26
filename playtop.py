import requests, re, time, os

category_dic = {
    "all": "全站榜",
    "origin": "原创榜",
    "rookie": "新人榜",
}

day_dic = {1: "日排行榜", 3: "三日排行榜", 7: "周排行榜", 30: "月排行榜"}
all_or_origin_dic = {
    0: "全站",
    1: "动画",
    168: "国创相关",
    3: "音乐",
    129: "舞蹈",
    4: "游戏",
    36: "科技",
    188: "数码",
    160: "生活",
    119: "鬼畜",
    155: "时尚",
    5: "娱乐",
    181: "影视",
}

bangumi_dic = {
    "番剧": 1,
    "国产动画": 4,
}

cinema_dic = {
    "记录篇": 177,
    "电影": 23,
    "电视剧": 11,
}

rookie_dic = {
    0: "全站",
    1: "动画",
    3: "音乐",
    129: "舞蹈",
    4: "游戏",
    36: "科技",
    188: "数码",
    160: "生活",
    119: "鬼畜",
    155: "时尚",
    5: "娱乐",
    181: "影视",
}

BaseDict = {
    "all": all_or_origin_dic,
    "origin": all_or_origin_dic,
    # "bangumi": bangumi_dic,
    # "cinema": cinema_dic,
    "rookie": rookie_dic,
}

a=time.strftime("%Y-%m-%d",time.localtime())

dic = {
    "all": 1,
    "origin": 2,
    "rookie": 3,
}

base_path = "./"       # 文件保存的位置


def get_url():
    for first in category_dic.keys():
        if first in ["all", "origin", "rookie"]:
            for second in BaseDict.get(first).keys():
                for third in day_dic.keys():
                    url = "https://api.bilibili.com/x/web-interface/ranking?jsonp=jsonp&rid={}&day={}&type={}&arc_type=0&callback=__jp1".format(
                        second, third, dic.get(first))
                    yield url, [first, second, third]

def  topm():
    os.mkdir(a)
    base_path = "./"+a+"/"
    s = requests.Session()
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": "https://www.bilibili.com/ranking/all/0/0/3"
    }
    url_list = get_url()
    dec=1
    for url in url_list:
        w=[]
        ww=[]
        print("向{}发请求".format(url[0]))
        response = s.get(url=url[0], headers=headers)
        data = response.text.replace('"', "")
        pattern = r'.*?aid:(?P<aid>.*?),.*?bvid:(?P<bvid>.*?),.*?author:(?P<author>.*?),.*?coins:(?P<coins>.*?),.*?duration:(?P<duration>.*?),.*?mid:(?P<mid>.*?),.*?cid:(?P<cid>.*?),.*?play:(?P<play>.*?),.*?pts:(?P<pts>.*?),.*?title:(?P<title>.*?),.*?video_review:(?P<video_review>.*?),'
        result_list = re.findall(pattern, data)
        path = os.path.join(base_path, "{}-{}-{}".format(category_dic.get(url[1][0]),
                                                     rookie_dic.get(url[1][1]) or all_or_origin_dic.get(url[1][1]),
                                                     day_dic.get(url[1][2])))
        f = open(path + ".txt", "a", encoding="utf-8")
        f.write(a)
        print('正在写入....{}'.format(path + ".txt"))
        www=0
        for index, res in enumerate(result_list):
            f.write("排名：{}\n".format(index + 1))
            f.write("AV号：{}\n".format(res[0]))
            f.write("BV号：{}\n".format(res[1]))
            f.write("标题：{}\n".format(res[9]))
            f.write("mid：{}\n".format(res[5]))
            f.write("作者：{}\n".format(res[2]))
            f.write("长度：{}\n".format(res[4]))
            f.write("播放量：{}\n".format(res[7]))
            f.write("投币数：{}\n".format(res[3]))
            f.write("弹幕数：{}\n".format(res[10]))
            f.write("综合分数：{}\n".format(res[8]))
            f.write("-" * 90 + "\n")
            www=www+1
            if www<=10:
                w.append(res[1])
                ww.append(res[0])
        f.close()
        if dec==1 :
            f=open("need2.txt", "w", encoding="utf-8")
            for i in w:
                qqq=str(i)+'\n'
                f.write(qqq)
            f.close()
            f=open("need3.txt", "w", encoding="utf-8")
            for i in ww:
                qqq=str(i)+'\n'
                f.write(qqq)
            f.close()
        time.sleep(2)
        dec=dec+1