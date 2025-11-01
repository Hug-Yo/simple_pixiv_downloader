from config import *
import requests
import json
from get_artworks_url import *
import re

# page = 1
# url = f'https://www.pixiv.net/ajax/search/illustrations/{s_tags}?word={s_tags}&order={s_order}&mode={s_age_mode}&scd={s_date}&p={page}&csw=0&s_mode=s_tag&type={s_type}&lang=en'
# res = requests.get(url,headers=headers)
# result = json.loads(res.text)
# # print(result)
# # print(type(result))
# # print(result['body']['illust']['data'])
# # print(type(result['body']['illust']['data']))
# # print(len(result['body']['illust']['data']))
#
# print(result['body']['illust']['data'][1])
# # print(len(result['body']['illust']['data']))
# # print(len(result['body']['illust']['data']))
# # print(len(result['body']['illust']['data']))
# # print(len(result['body']['illust']['data']))
# title = result['body']['illust']['data'][1]['title']
# tags = result['body']['illust']['data'][1]['tags']
# url = re.sub(r'/c/\d+x\d+_\d+_a\d+/|square1200', lambda m: '/' if 'c/' in m.group(0) else 'master1200', result['body']['illust']['data'][1]['url'])
# illust_type = result['body']['illust']['data'][1]['illustType']
# user_id = result['body']['illust']['data'][1]['userId']
# pid = result['body']['illust']['data'][1]['id']
# pages = result['body']['illust']['data'][1]['pageCount']
# print(title)
# print(tags)
# print(result['body']['illust']['data'][1]['url'])
# print(url)
# print(illust_type)
# print(user_id)
# print(pid)
# print(pages)
#
# res = requests.get(url,headers=headers)
# with open('test.png','wb') as f:
#     f.write(res.content)

url = 'https://www.pixiv.net/ajax/search/illustrations/血小板?word=血小板&order=date_d&mode=r18&scd=1900-01-01&p=2&csw=0&s_mode=s_tag&type=illust_and_ugoira&lang=en'
res = requests.get(url,headers=headers)
result = json.loads(res.text)


def extract_artwork_info(data):
    """提取作品信息"""
    search_artwork_list = []

    # 从 popular -> permanent 中提取作品信息
    for item in data['body']['popular']['permanent']:
        pid= item['id']
        title= item['title']
        tags= item['tags']
        url= item['url']
        illust_type= item['illustType']
        user_id= item['userId']
        pages= item['pageCount']
        search_artwork_list.append(Artwork(title, tags, url, illust_type, user_id, pid, pages))

    return search_artwork_list

a = extract_artwork_info(result)
print(a)

# for page in range(1, 11):
#     pid_list = []
#     url = f'https://www.pixiv.net/ajax/search/illustrations/{s_tags}?word={s_tags}&order={s_order}&mode={s_age_mode}&scd={s_date}&p={page}&csw=0&s_mode=s_tag&type={s_type}&lang=en'
#     print(url)
#     res = requests.get(url,headers=headers)
#     result = json.loads(res.text)
#     print(res.status_code)
#     print(result)
    # for _ in range(len(result['body']['illust']['data'])):
    #     pid =result['body']['illust']['data'][_]['id']
    #     pid_list.append(pid)
    # print(f'第{page}页pid为',pid_list)