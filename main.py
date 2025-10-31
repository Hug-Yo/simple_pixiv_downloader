from config import mode,content,n_artwork,if_return_all
import time
import get_artworks_url

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print("welcome to pixiv_downloader")
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
    art_work_url = get_artworks_url.get_artworks_url()
    print("url获取成功")
    print("开始下载...")
    get_artworks_url.download_artwork(n_artwork,art_work_url)
    print("下载结束...")