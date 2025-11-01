from config import *
import time
import get_artworks_url
import downloader
from get_artworks_url import get_search_artworks_url

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    while True:
        print("welcome to pixiv_downloader")
        ans = input('''
请选择模式：
下载排行榜作品(press 1)
下载搜索作品(press 2)
结束程序(press 3)
''')
        if ans == '1':
            print(f'''
下载设置预览：
mode : {mode}
content : {content}
n_artwork : {n_artwork}(默认0为前50张)
抓取全部 : {if_return_all}
''')
            print("正在获取url...")
            artwork_ranking_list = get_artworks_url.get_ranking_artworks_url()
            print('url获取完成')
            # 是否启用多页下载模式
            if multi_pages_download:
                downloader.multi_pages_download(artwork_ranking_list)
            print("开始下载...")
            downloader.download_ranking_artwork(n_artwork,artwork_ranking_list)
            print("下载结束...")
            continue
        elif ans == '2':
            print('正在获取url...')
            search_artwork_list = get_artworks_url.get_search_artworks_url()
            print('url获取完成')
            #是否启用多页下载模式
            if multi_pages_download:
                downloader.multi_pages_download(search_artwork_list)
            #是否启用排序模式并选择排序模式
            if ranking_mode:
                while True:
                    if_rank = input('''
请选择排序方式
按喜欢数(press 1):
按订阅数(press 2):
按浏览数(press 3):
''')
                    if if_rank == '1':
                        search_artwork_list.sort(key=lambda x:x.like_count, reverse=True)
                        break
                    elif if_rank == '2':
                        search_artwork_list.sort(key=lambda x:x.bookmark_count, reverse=True)
                        break
                    elif if_rank == '3':
                        search_artwork_list.sort(key=lambda x:x.view_count, reverse=True)
                        break
                    else:
                        continue
            downloader.download_search_artworks(search_artwork_list,ranking_mode_download_limit)
            print('下载结束')
            continue

        elif ans == '3':
            print('退出程序')
            break
        else:
            print('输入有误，请重新输入')
            continue