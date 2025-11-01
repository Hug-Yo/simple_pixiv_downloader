import datetime
from datetime import timedelta
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
ranking_mode_download_limit = 20 #如启用ranking_mode，下载排名前20的图片
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
#--------------------------------


#user_config
#--------------------------------
#若需要下载r18类作品请用浏览器登陆自己的pixiv账号，抓取cookie
cookies = 'first_visit_datetime_pc=2025-10-19%2013%3A14%3A25; p_ab_id=2; p_ab_id_2=9; p_ab_d_id=2012437270; yuid_b=M5czgFU; _ga=GA1.1.1835298157.1760847268; device_token=96aaf53df213c1125cfb3c2db4e9c76f; privacy_policy_agreement=7; c_type=51; privacy_policy_notification=0; a_type=1; b_type=1; _gcl_au=1.1.1989850141.1760847526; login_ever=yes; PHPSESSID=44858349_ydu5aVmq9oT3dEgXQ32hhyu7vI43K0t5; _ga_MZ1NL4PHH0=GS2.1.s1761313124$o3$g1$t1761313137$j47$l0$h0; _im_vid=01K8WM5RZPMMHQBPGDKNNQRE5Z; __bnc_pfpuid__=16vr-l3TV1BnjMX; _cfuvid=VHNrxzya050L9nG_C5rweSeza.iYEhibmcV8K2bY3vQ-1761907803442-0.0.1.1-604800000; __cf_bm=YxIMxumgePn_a9rwD7NjucdIkNExJk3PcxFvbXloGYI-1761919390-1.0.1.1-At.M69jpuZ2pziNi3NIToHOW6B_4K2t5q0rAdBLOL8Ej537jx6CciPhM8izdiLuKGTznz6p53sea98lpkACHnpMIm63bENyzLYYIMPxcGM.OVJ2dQuEqEOPcekMViVzm; _ga_75BBYNYN9J=GS2.1.s1761919746$o11$g0$t1761919746$j60$l0$h0; cf_clearance=U6i8g0lTwNUhpRGTPmjqCQjggGBlM08dkX4hIepJHIg-1761919744-1.2.1.1-az4Q5P9kcQfoXgL.UU1n9aP88pxE3OVvFKQj_aGi9yG6u0Ef18oqUz_1zmGg4s7pds_u9dpbCfnE13v5xRds.hU3GyogpJQXKEzO2Abuz1XrGbiho9tnWy2tPnVW8w2AtYeq4Q_lAnpWfu1ZjSi6Veejf.9VOWEE5gCbDx70qDcb32Jf45aS5q.H9GKcw4kcmekfXk1Zbp5YrbOf1jGBHFDA7iGrxRG9gSyEvesj2wg'
#--------------------------------


#下面两项一般情况下无需更改
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
headers = {"User-Agent": user_agent,
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