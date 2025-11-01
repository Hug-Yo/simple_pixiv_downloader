from config import mode,content,n_artwork,if_return_all
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
            print("5s后开始下载...")
            time.sleep(5)
            print("正在获取url...")
            art_work_url = get_artworks_url.get_ranking_artworks_url()
            print("url获取成功")
            print("开始下载...")
            downloader.download_ranking_artwork(n_artwork,art_work_url)
            print("下载结束...")
            continue
        elif ans == '2':
            search_artwork_list = get_artworks_url.get_search_artworks_url()
            #多页下载模式
            downloader.multi_pages_download(search_artwork_list)
            downloader.download_search_artworks(search_artwork_list)
            print('下载结束')
            continue

        elif ans == '3':
            print('退出程序')
            break
        else:
            print('输入有误，请重新输入')
            continue