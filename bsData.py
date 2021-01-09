from bs4 import BeautifulSoup
import requests
import time


url = "https://www.msn.com/th-th/news/national/ข่าวดีแรงงาน-ประกันสังคมแจ้งผู้รับผลกระทบโควิด-ยื่นรับสิทธิว่างงาน-ดีเดย์-4-มกราคมนี้/ar-BB1cqX4N"

res = requests.get(url)
res.encoding = "utf-8"
print(res)
if res.status_code == 200:
    print("Successful")
else:
    print("Error")
# time.sleep(5)
soup = BeautifulSoup(res.text, 'html5lib')
# print(soup.prettify())
title = soup.title.string
print(title)
h1 = soup.h1.string
if(h1 != None and h1 != title):
    print(h1)
else:
    None
h2 = soup.h2.string
if(h2 != None and h2 != h1):
    print(h2)
else:
    None
# h3 = soup.h3.string
# if(h3 != None):
#     print(h3)
# else:
#     None
p_list = []
p = soup.find_all('p')
if(p != None):
    for data in p:
        obj = data.string
        p_list.append(obj)
    print(p_list)
else:
    None

sp_list = []
sp = soup.find_all('span')
if(sp != None):
    for data in sp:
        obj = data.string
        sp_list.append(obj)
    print(sp_list)
else:
    None


# body = soup.body.string
# if(body != None):
#     print(body)
# else:
#     None
# content_list = []
# content = soup.find_all('content')
# if(content != None):
#     for data2 in content:
#         obj = data2.string
#         content_list.append(obj)
#     print(content_list)
# else:
#     None



# Specific for pantip
# content = soup.display-post-story.string
# print(content)