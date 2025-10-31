import requests
import json
import os
from config import start_date,mode,if_return_all,headers,content

#定义画作的类
class Artwork:
    def __init__(self,title,tags,url,illust_type,user_id):
        self.title = title
        self.tags = tags
        self.url = url
        self.illust_type = illust_type
        self.user_id = user_id

def get_artworks_url():
    # 获取pixiv排行榜所有画作信息，共十页
    art_work_list = []
    for _ in range (1,11):
        try:
            #向服务器发出get请求，获取排行榜的json包
            req = requests.get(f'https://www.pixiv.net/ranking.php?mode={mode}&content={content}&date={start_date}&p={_}&format=json',headers=headers)
            result = json.loads(req.text)  #得到字典类型result
            for __ in range (len(result['contents'])):
                title = result['contents'][__]['title']
                tags = result['contents'][__]['tags']
                url = result['contents'][__]['url']
                illust_type = result['contents'][__]['illust_type']
                user_id = result['contents'][__]['user_id']
                art_work_list.append(Artwork(title,tags,url,illust_type,user_id))
        except Exception as e:
            break
    return art_work_list

#进行画作筛选以及下载数量限制
def download_artwork(n_artwork,art_work_list):
    if not os.path.exists(f'./pixiv_images/{start_date}'):
        os.makedirs(f'./pixiv_images/{start_date}')
        print("目录创建成功")
    else:
        print("目录已存在")
    if n_artwork != 0 and if_return_all == False:
        for _ in range (n_artwork):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{art_work_list[_].title}{mode}.png','wb') as f:
                f.write(req.content)
    elif n_artwork == 0 and if_return_all == False:
        for _ in range (50):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{art_work_list[_].title}{mode}.png','wb') as f:
                f.write(req.content)
    elif if_return_all:
        for _ in range (len(art_work_list)):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{art_work_list[_].title}{mode}.png','wb') as f:
                f.write(req.content)
