import requests
import json
from config import s_order,s_age_mode,page_limit,s_type,s_date,s_tags
# import downloader
# from downloader import multi_pages_download
import re
from config import start_date,mode,if_return_all,headers,content

#定义画作的类
class Artwork:
    def __init__(self,title,tags,url,illust_type,user_id,pid,pages):
        self.title = title
        self.tags = tags
        self.illust_type = illust_type
        self.user_id = user_id
        self.url = []
        self.url.append(url)
        self.pid = pid
        self.pages = pages
    def multi_pages_mode(self):
        if self.pages == '1':
            return
        else:
            for index in range(1,int(self.pages)):
                try:
                    pattern = r'(.*)_p(\d+)_(.*)'
                    match = re.match(pattern, self.url[0])
                    prefix, _, suffix = match.groups()
                    self.url.append(f'{prefix}_p{index}_{suffix}')
                except:
                    break

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
                #解包result，提取关键信息并创建Artwork对象
                for __ in range (len(result['contents'])):
                    title = result['contents'][__]['title']
                    tags = result['contents'][__]['tags']
                    url = re.sub(r'/c/\d+x\d+/', '/', result['contents'][__]['url'])
                    illust_type = result['contents'][__]['illust_type']
                    user_id = result['contents'][__]['user_id']
                    pid = result['contents'][__]['illust_id']
                    pages = result['contents'][__]['illust_page_count']
                    art_work_list.append(Artwork(title, tags, url, illust_type, user_id, pid,pages))
                print(f'第{_}页获取成功')
            except:
                print(f'第{_}页获取失败，可能资源并不存在，已跳过')
        except Exception as e:
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
            res = requests.get(url,headers=headers)
            result = json.loads(res.text)
            if False:
                try:
                    for item in result['body']['popular']['permanent']:
                        pid = item['id']
                        title = item['title']
                        tags = item['tags']
                        url = re.sub(r'/c/\d+x\d+_\d+_a\d+/|square1200', lambda m: '/' if 'c/' in m.group(0) else 'master1200', item['url'])
                        illust_type = item['illustType']
                        user_id = item['userId']
                        pages = item['pageCount']
                        search_artwork_list.append(Artwork(title, tags, url, illust_type, user_id, pid, pages))
                        print(url)
                    print(f'第{page}页获取成功')
                except:
                    print(f'第{page}页获取失败，结束获取')
                    break
            else:
                try:
                    for item in result['body']['illust']['data']:
                        pid = item['id']
                        title = item['title']
                        tags = item['tags']
                        url = re.sub(r'/c/\d+x\d+_\d+_a\d+/|square1200', lambda m: '/' if 'c/' in m.group(0) else 'master1200', item['url'])
                        illust_type = item['illustType']
                        user_id = item['userId']
                        pages = item['pageCount']
                        search_artwork_list.append(Artwork(title, tags, url, illust_type, user_id, pid, pages))
                        # print(url)
                    print(f'第{page}页获取成功')
                except:
                    print(f'第{page}页获取失败，结束获取')
                    break
            page += 1
        except:
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