import requests
import time
#主要是调用B站的API来实现刷播放量
#首先先定义它的headers，在我们点击视频的时候，查看它的xhr，然后我们就可以找到它的对应cookie了，因为怎么获取播放量和cookie有关
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive',
    'referer': 'https://www.bilibili.com/video/BV1iC4y1p7Um/',
    "cookie": "_uuid=3A318514-7B21-7F9B-715D-5358FA315D0D11914infoc; buvid3=7B7F7CFF-E0CE-4317-AC2C-C8ADF975289253920infoc; sid=9sbfkfld; CURRENT_FNVAL=16; rpdid=|(uYm~YJm))l0J'ul))R)u~YJ; LIVE_BUVID=AUTO6015884836169069; CURRENT_QUALITY=80; bp_t_offset_35906556=392132580010163986; PVID=3; DedeUserID=35906556; DedeUserID__ckMd5=6bc77a6b9c4d788a; SESSDATA=c7a7e24c%2C1605943181%2C95472*51; bili_jct=d263a22829f9bad2b775aa9813ccf5d1; bp_video_offset_35906556=393915923444549998; bfe_id=da609d6ad479671e4cd33f2670c43937",

}
stime = str(int(time.time()))
#获取我们要刷这个视频的data数据
data= {
    'aid':'795857643',
    'cid':'195581731',
    "bvid": "BV1iC4y1p7Um",
    'part':'1',
    'mid':'35906556',
    'lv':'5',
    "stime" :stime,
    'jsonp':'jsonp',
    'type':'3',
    'sub_type':'0',
}
#然后就先是解析这个页面了
def get_html(url):
    count = 0
    while True:
        try:
            #发起一个post请求，去请求这个页面，从而获得一次点击量
            req = requests.post(url,data=data,headers=headers)
            count += 1
            print("now in loop {}".format(count))
            print(req.text)
            #这里设置等待时间，因为B站的时间间隔是400秒的，当然如果你是用IP池的可以随便浪
            time.sleep(100)
        except Exception as e:
            print(e)
            time.sleep(100)
            print('over')
    print("over")

if __name__ == '__main__':
    url = "https://api.bilibili.com/x/click-interface/click/web/h5"
    get_html(url)

