# simple_pixiv_downloader
## 简介
这是本人初学python的简易项目，仅供练习使用
## config  设置
```python
mode = 'daily_r18'
content = 'illust'
n_artwork = 10
if_return_all = False
```
### 说明：
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

user_agent和header一般情况下无需改动

>关于pixiv画作参数详情:https://natescarlet.github.io/pixiv/artwork_rank.html
