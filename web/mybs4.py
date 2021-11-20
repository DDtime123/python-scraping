import requests
from bs4 import BeautifulSoup

questions = []
announces = []

URL = 'http://www.51mxd.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(URL,headers=headers)
#print(page.headers)

soup = BeautifulSoup(page.content,'html.parser')
"""
# 按ID查找元素
results = soup.find(id="soundplayerlayer")
print(type(soup))
print(type(results))
print(type(results.prettify()))
print(results.prettify())
"""
"""
# 按类名查找元素
"""

project_elements = soup.findAll("td",{"class":"probname tal"})
for element in project_elements:
    #print(element.find("a")['tppabs'])
    #print(element.find("a").getText(),end="\n")
    questions.append([element.find("a").getText(),element.find("a")['tppabs']])


URL = 'http://news.cqjtu.edu.cn/xxtz.htm'
page = requests.get(URL,headers=headers)
page.raise_for_status()
soup = BeautifulSoup(page.content,'html.parser')
results = soup.findAll("div",{"class":"right-title"})
for result in results:
    #print(result.find("a")['title'])
    #print(result.find("a")['href'],end="\n")
    announces.append([result.find("a")['title'],result.find("a")['href']])

with open("question.txt","w") as f:
    for question in questions:
        f.write(question[0]+" "+ question[1]+"\n")

with open("announce.txt","w") as f:
    for announce in announces:
        f.write(announce[0]+" "+ announce[1]+"\n")