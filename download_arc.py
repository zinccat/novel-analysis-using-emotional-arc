# 下载对应的情感弧文件
from selenium import webdriver
import os
os.chdir('./data')
if not os.path.exists('./detective'):
    os.makedirs('./detective')
os.chdir('./detective')

# 使用selenium爬取情感弧
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
options.add_argument('--disable-gpu')
# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')
# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
options.add_argument('--headless')
path = '../../chromedriver'
driver = webdriver.Chrome(options=options, executable_path=path)

with open('../real_detective.txt', 'r') as f:
    a = f.readlines()
    for num in a:
        url = 'http://hedonometer.org/data/bookdata/gutenberg-007/' + \
            num[:-1] + '.csv'
        driver.get(url)
