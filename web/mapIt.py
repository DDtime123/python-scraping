"""
import webbrowser as wb

wb.open('https://inventwithpython.com/') # 打开默认浏览器，并开启网页
"""

import requests
res = requests.get('https://automatetheboringstuff.com/2e/chapter12/') # 返回 response
res.raise_for_status()

# 保存文件
playFile = open('./file.txt', 'wb') # 打开文件

for chunk in res.iter_content(100000): # 将 response 中的文本写入文件
    playFile.write(chunk)
    
playFile.close() # 关闭文件