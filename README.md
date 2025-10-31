from gettext import install

# simple_pixiv_downloader
## 简介
这是本人初学python的简易项目，仅供练习使用
依赖安装：
```
pip install os
pip install requests
pip install json
```
## config  设置
```python
start_time = ''
mode = 'daily_r18'
content = 'illust'
n_artwork = 10
if_return_all = False
```
### 说明：
`start_time`日期格式为YYMMDD,默认为最新排行榜

`mode`可选值有[diary,weekly,monthly,rookie,original,male,female,daily_r18,weekly_r18,male_r18,female_r18,r18,r18g]

`content`可选值[illust,ugoira,manga]

`n_artwork`下载作品数量，如设置为0则表示默认（前50张）

`if_return_all`是否下载全部作品

*注意，由于本项目未限制请求频率，如`if_return_all`设置为`True`,请求频率过高可能导致被pixiv屏蔽*

## user_config 设置
```python
cookies = ''
user_agent =''
headers =''
```
### 说明：
若cookie留空，则mode不可选择[daily_r18,weekly_r18,male_r18,female_r18,r18]

cookie具有时效性，如下载失败请尝试更新cookie

user_agent和header一般情况下无需改动

下载地址为当前目录下创建的`/pixiv_image/{date}`

>关于pixiv画作参数详情:https://natescarlet.github.io/pixiv/artwork_rank.html
