import requests
import os
from config import *

#排行榜下载
def download_ranking_artwork(n_artwork,art_work_list):
    #检测目录是否已存在，若否，则创建目录
    if not os.path.exists(f'./pixiv_images/{start_date}/{mode}'):
        os.makedirs(f'./pixiv_images/{start_date}/{mode}')
        print("目录创建成功")
    else:
        print("目录已存在")
    #根据n_artwork和if_return_all的值来确定下载排行榜前多少张的图片,若if_return_all==ture则忽略n_artwork，下载所有图片
    extent = 0
    if n_artwork != 0 and if_return_all == False:
        extent = n_artwork
    elif n_artwork == 0 and if_return_all == False:
        extent = 50
    elif if_return_all:
        extent = len(art_work_list)
    for _ in range (extent):
        print(art_work_list[_].url)
        i = 1
        for url in art_work_list[_].url:
            try:
                req = requests.get(url,headers=headers)
                with open(f'./pixiv_images/{start_date}/{mode}/{art_work_list[_].pid}{mode}--page{i}.png','wb') as f:
                    f.write(req.content)
                i = i + 1
                print(f'本张写入完成')
            except Exception as e:
                print(e)
    print(f'下载完成')

#某画师作品下载
def download_users_artworks():
    pass


#下载某搜索结果的内容
def download_search_artworks(search_artwork_list,num):
    if not os.path.exists(f'pixiv_images/{s_tags}'):
        os.makedirs(f'pixiv_images/{s_tags}')
        print("目录创建成功")
    else:
        print("目录已存在")
    if not ranking_mode:
        num = len(search_artwork_list)
    for index in range (num):
        item = search_artwork_list[index]
        if item.illust_type == '2' or item.illust_type == 2:
            continue
        else:
            try:
                _ = 0
                for _ in range (len(item.url)):
                    res = requests.get(item.url[_],headers=headers)
                    with open(f'pixiv_images/{s_tags}/{item.pid}-page{_+1}（{item.bookmark_count}订阅）.png','wb') as f:
                        f.write(res.content)
                    print('本张写入完成')
            except BaseException as e:
                print(e)
                continue
    print('下载完成')


#启用多页下载,若不调用此函数则默认下载作品首页
def multi_pages_download(art_work_list):
    for item in art_work_list:
        item.multi_pages_mode()