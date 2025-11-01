import datetime
from datetime import timedelta
from fake_useragent import UserAgent
ua = UserAgent()
#默认开始时间，不用修改
def get_target_date():
    now = datetime.datetime.now()
    # 判断当前时间是否在中午12点之前
    if now.hour < 12:
        # 中午12点之前，返回前天日期
        target_date = now - timedelta(days=2)
    else:
        # 中午12点之后，返回昨天日期
        target_date = now - timedelta(days=1)
    return target_date.strftime('%Y%m%d')
start_date = get_target_date()


#基础设置
#--------------------------------
multi_pages_download = True  #是否启用多页下载
ranking_mode = True  #是否启用排序模式（极慢）

#--------------------------------

#排行榜模式设置
#--------------------------------
start_date = start_date  #日期格式为YYMMDD,默认为最新排行榜
mode = 'daily'  #可选值[daily,weekly,monthly,rookie,original,male,female,daily_r18,weekly_r18,male_r18,female_r18,r18g]
content = 'illust' #可选值[illust,ugoira,manga]
n_artwork = 10 #返回作品数量,设置为0代表默认前50张
if_return_all = True #是否输出所有抓取到的画作信息（不建议开启）
#--------------------------------

#tag搜索模式设置
#--------------------------------
s_order = 'date_d'
s_age_mode = 'safe'
page_limit = 15
s_type = 'illust_and_ugoira'
s_tags = 'miku'
ranking_mode_download_limit = 50 #如启用ranking_mode，下载排名前n的图片
#--------------------------------


#user_config
#--------------------------------
#若需要下载r18类作品请用浏览器登陆自己的pixiv账号，抓取cookie
cookies = ''
#--------------------------------


#下面两项一般情况下无需更改
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
headers = {"User-Agent": ua.random,
           "cookie": cookies,
           "referer":"https://www.pixiv.net",
           "Accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
           "Accept-Encoding":"gzip, deflate, br, zstd",
           "Cache-Control":"no-cache",
           "Connection":"keep-alive",
           "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
           "pragma":"no-cache",
           "priority":"u=1, i",
           "sec-ch-ua":'sec-ch-ua"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
           "sec-ch-ua-mobile":"?0",
           "sec-ch-ua-platform":"windows",
           "sec-fetch-dest":"image",
           "sec-fetch-mode":"no-cors",
           "sec-fetch-site":"cross-site",
           "sec-fetch-storage-access":"active"
           }