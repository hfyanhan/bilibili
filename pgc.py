
import requests, re, time, os

category_dic = {
	"bangumi": "新番榜",
	"cinema": "影视榜",
}

day_dic = { 3: "三日排行榜", 7: "周排行榜"}


bangumi_dic = {
	1 :  "番剧",
	4 : "国产动画",
}


cinema_dic = {
	3 : "纪录片",
	2 : "电影" ,
	5 : "电视剧",
}

BaseDict = {

	"bangumi": bangumi_dic,
	"cinema": cinema_dic,
}

a=time.strftime("%Y-%m-%d",time.localtime())


base_path = "./"       # 文件保存的位置


def get_url():
	for first in category_dic.keys():
		if first in ["bangumi", "cinema"]:
			for second in BaseDict.get(first).keys():
				for third in day_dic.keys():
					url = "https://api.bilibili.com/pgc/web/rank/list?day={}&season_type={}".format(
						third, second)
					yield url, [first, second, third]

def  topm():
	try:
		os.mkdir(a)
	except Exception:
		print("Already")
	base_path = "./"+a+"/"
	s = requests.Session()
	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
	"Referer": "https://www.bilibili.com/ranking/all/0/0/3"
	}
	url_list = get_url()
	for url in url_list:
		print("向{}发请求".format(url[0]))
		response = s.get(url=url[0], headers=headers)
		data = response.text
		path = os.path.join(base_path, "{}-{}-{}".format(category_dic.get(url[1][0]),
													 cinema_dic.get(url[1][1]) or bangumi_dic.get(url[1][1]),
													 day_dic.get(url[1][2])))
		f = open(path + ".txt", "a", encoding="utf-8")
		f.write(data)
		print('正在写入....{}'.format(path + ".txt"))
		f.close()
		time.sleep(2)