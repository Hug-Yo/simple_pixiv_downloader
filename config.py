import datetime
from datetime import timedelta
#默认开始时间，不用修改
start_date = (datetime.date.today() - timedelta(days=1)).strftime('%Y%m%d')

#mode_config
#--------------------------------
start_date = start_date  #日期格式为YYMMDD,默认为最新排行榜
mode = 'weekly_r18'  #可选值[diary,weekly,monthly,rookie,original,male,female,daily_r18,weekly_r18,male_r18,female_r18,r18,r18g]
content = 'illust' #可选值[illust,ugoira,manga]
n_artwork = 10 #返回作品数量,设置为0代表默认前50张
if_return_all = False #是否输出所有抓取到的画作信息（不建议开启）

##################################

#user_config
#--------------------------------
#若需要下载r18类作品请用浏览器登陆自己的pixiv账号，抓取cookie
cookies = ''

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