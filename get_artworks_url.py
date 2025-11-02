import requests
import json
from config import *
import time
import re


#定义画作的类
class Artwork:
    def __init__(self,title,tags,url,illust_type,user_id,pid,pages,like_count,view_count,bookmark_count):
        self.title = title
        self.tags = tags
        self.illust_type = illust_type
        self.user_id = user_id
        self.url = []
        self.url.append(url)
        self.pid = pid
        self.pages = pages
        self.like_count = like_count
        self.view_count = view_count
        self.bookmark_count = bookmark_count
        #启用多页下载，若想启用多页下载，调用此类函数即可
    def multi_pages_mode(self):
        if self.pages == '1' or self.pages == 1 :
            return
        else:
            for index in range(1,int(self.pages)):
                try:
                    #正则准备
                    pattern = r'_p\d+_'  # 匹配 _p数字_ 的模式
                    replacement = f'_p{index}_'
                    self.url.append(re.sub(pattern, replacement, self.url[0]))
                except Exception as e:
                    print(e)
                    break


#获取排行榜作品的基础信息
def get_ranking_artworks_info(item):
    #遍历result，result是字典类型，通过此方法获取所需的化作信息
    pid = item['illust_id']
    title = item['title']
    tags = item['tags']
    url = re.sub(r'/c/\d+x\d+/', '/', item['url'])
    illust_type = item['illust_type']
    user_id = item['user_id']
    pages = item['illust_page_count']
    return title,tags,url,illust_type,user_id,pid,pages



#获取tag搜索作品基础信息
def get_artworks_info(item):
    #遍历result，result是字典类型，通过此方法获取所需的化作信息
    pid = item['id']
    title = item['title']
    tags = item['tags']
    url = re.sub(r'/c/\d+x\d+_\d+_a\d+/|square1200',
                 lambda m: '/' if 'c/' in m.group(0) else 'master1200',
                 item['url'])
    #正则准备
    pattern = r'https://i\.pximg\.net/custom-thumb/img/(\d{4}/\d{2}/\d{2}/\d{2}/\d{2}/\d{2}/(\d+)_p(\d+))_custom1200\.jpg'
    replacement = r'https://i.pximg.net/img-master/img/\1_master1200.jpg'
    #正则转化
    url = re.sub(pattern, replacement, url)
    illust_type = item['illustType']
    user_id = item['userId']
    pages = item['pageCount']
    return title,tags,url,illust_type,user_id,pid,pages

#获取作品的热度信息
def get_artworks_pop_info(item):
    #获取pid，为获取pop_info做准备
    pid = item['id']
    #这是作品详情页的数据，返回json包
    url = f'https://www.pixiv.net/ajax/illust/{pid}'
    i = 0
    while i <= 3:
        try:
            res = requests.get(url,headers=headers)
            print(f'本张热度信息获取完成')
            time.sleep(1)
            break
        except Exception as e:
            print(e)
            print(f'获取失败，正在重试，剩余次数{2-i}')
            i += 1
            time.sleep(1)
            continue
    #解包json
    result = json.loads(res.text)
    like_count = result['body']['likeCount']
    view_count = result['body']['viewCount']
    bookmark_count = result['body']['bookmarkCount']
    return like_count,view_count,bookmark_count




#排行榜url抓取
def get_ranking_artworks_url():
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
                #遍历result字典，调用函数解包result，提取关键信息并创建Artwork对象
                for item in result['contents']:
                    #调用函数获取item（某一作品）的info，并赋值给art_work_info,此函数的返回值为一系列如title，pid登信息
                    art_work_info = get_ranking_artworks_info(item)
                    #初始化 热度 信息，若未开启排行模式则跳过获取热度信息这一步
                    artwork_pop_info = (0,0,0)
                    #将info，pop_info解包传入自定义类，并将自定义类放进art_work_list
                    art_work_list.append(Artwork(*art_work_info,*artwork_pop_info))
                print(f'第{_}页获取成功')
            except BaseException as e:
                print(e)
                print(f'第{_}页获取失败，可能资源并不存在，已跳过')
        except Exception as e:
            print(e)
            break
    return art_work_list




#抓取某一个作者的全部作品url
def get_users_artworks_url():
    art_work_list = []
    user_id = input("请输入作者pid:")
    while True:
        try:
            url = f'https://www.pixiv.net/en/users/{user_id}/artworks'
            req = requests.get(url,headers=headers)
            result = json.loads(req.text)
        except:
            pass
        pass  #作者详情页疑似被加密，暂时无法解决




#抓取某一搜索结果的所有作品url
def get_search_artworks_url():
    page = 1
    search_artwork_list = []
    while page <= page_limit:
        try:
            url = f'https://www.pixiv.net/ajax/search/illustrations/{s_tags}?word={s_tags}&order={s_order}&mode={s_age_mode}&p={page}&csw=0&s_mode=s_tag&type={s_type}&lang=en'
            i = 1
            while i <= 3:
                try:
                    res = requests.get(url,headers=headers)
                    break
                except BaseException as e:
                    print(e)
                    i += 1
                    continue
            result = json.loads(res.text)
            try:
                for item in result['body']['illust']['data']:
                    #下面调用的两个函数分别用于获取作品的基础信息和热度信息
                    art_work_info = get_artworks_info(item)
                    artwork_pop_info = (0,0,0)
                    if ranking_mode:
                        artwork_pop_info = get_artworks_pop_info(item)
                    #解包赋值创建Artwork类
                    search_artwork_list.append(Artwork(*art_work_info,*artwork_pop_info))
                print(f'第{page}页获取成功')
            except BaseException as e:
                print(e)
                print(f'第{page}页获取失败，结束获取')
                break
            page += 1
        except BaseException as e:
            print(e)
            break
    return search_artwork_list

if __name__ == '__main__':
    search_artwork_list = get_search_artworks_url()


#用于设置断点debug
# if __name__ == '__main__':
    # art_work_list = get_ranking_artworks_url()
    # downloader.multi_pages_download(art_work_list)
    # for item in art_work_list:
    #     for _ in range (len(item.url)):
    #         print(item.url[_])