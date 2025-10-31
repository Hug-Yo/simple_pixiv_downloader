import requests
import json
import os
import re
from config import start_date,mode,if_return_all,headers,content

#定义画作的类
class Artwork:
    def __init__(self,title,tags,url,illust_type,user_id,pid):
        self.title = title
        self.tags = tags
        self.illust_type = illust_type
        self.user_id = user_id
        self.url = url
        self.pid = pid

def get_artworks_url():
    # 获取pixiv排行榜所有画作信息，最多十页
    art_work_list = []
    for _ in range (1,11):
        url = [f'https://www.pixiv.net/ranking.php?mode={mode}&content={content}&date={start_date}&p={_}&format=json',
               f'https://www.pixiv.net/ranking.php?mode={mode}&date={start_date}&p={_}&format=json',
               f'https://www.pixiv.net/ranking.php?mode={mode}&p={_}&format=json']
        try:
            #向服务器发出get请求，获取排行榜的json包
            if mode == 'original':
                req = requests.get(url[2],headers=headers)
            elif mode in ['male', 'female', 'male_r18', 'female_r18']:
                req = requests.get(url[1],headers=headers)
            else:
                req = requests.get(url[0],headers=headers)
            result = json.loads(req.text)  #得到字典类型result
            try:
                #解包result，提取关键信息并创建Artwork对象
                for __ in range (len(result['contents'])):
                    title = result['contents'][__]['title']
                    tags = result['contents'][__]['tags']
                    url = re.sub(r'/c/\d+x\d+/', '/', result['contents'][__]['url'])
                    illust_type = result['contents'][__]['illust_type']
                    user_id = result['contents'][__]['user_id']
                    try:
                        pid = re.findall(r'/(\d+)_p\d', url)[0]
                    except:
                        pid = re.findall(r'/(\d+)_', url)[0]
                    art_work_list.append(Artwork(title, tags, url, illust_type, user_id, pid))
                    art_work_list.append(Artwork(title,tags,url,illust_type,user_id,pid))
                print(f'第{_}页获取成功')
            except:
                print(f'第{_}页获取失败，可能资源并不存在，已跳过')
        except Exception as e:
            break
    return art_work_list

#进行画作筛选以及下载数量限制
def download_artwork(n_artwork,art_work_list):
    #检测目录是否已存在，若否，则创建目录
    if not os.path.exists(f'./pixiv_images/{start_date}/{mode}'):
        os.makedirs(f'./pixiv_images/{start_date}/{mode}')
        print("目录创建成功")
    else:
        print("目录已存在")
    #根据n_artwork和if_return_all的值来确定下载排行榜前多少张的图片,若if_return_all==ture则忽略n_artwork，下载所有图片
    if n_artwork != 0 and if_return_all == False:
        for _ in range (n_artwork):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{mode}/{art_work_list[_].pid}{mode}.png','wb') as f:
                f.write(req.content)
    elif n_artwork == 0 and if_return_all == False:
        for _ in range (50):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{mode}/{art_work_list[_].pid}{mode}.png','wb') as f:
                f.write(req.content)
    elif if_return_all:
        for _ in range (len(art_work_list)):
            req = requests.get(art_work_list[_].url,headers=headers)
            with open(f'./pixiv_images/{start_date}/{mode}/{art_work_list[_].pid}{mode}.png','wb') as f:
                f.write(req.content)

#用于设置断点debug
if __name__ == '__main__':
    art_work_list = get_artworks_url()
    for _ in range (len(art_work_list)):
        print(art_work_list[_].url)