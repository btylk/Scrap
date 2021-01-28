from bs4 import BeautifulSoup
import requests
import time
import json

url = "https://www.sanook.com/news/8341106/"

res = requests.get(url)
res.encoding = "utf-8"
# print(res)
if res.status_code == 200:
    print("Successful")
else:
    print("Error")
# time.sleep(5)
soup = BeautifulSoup(res.text, 'html5lib')
# print(soup.prettify())
title = soup.title.string
# print(title)
h1 = soup.h1.string
if(h1 != None and h1 != title):
    pass
else:
    None
h2 = soup.h2.string
if(h2 != None and h2 != h1):
    pass
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
    # print(p_list)
else:
    None

sp_list = []
sp = soup.find_all('span')
if(sp != None):
    for data in sp:
        obj = data.string
        sp_list.append(obj)
    # print(sp_list)
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

data = {'Data':[{'Title': title}]}
export_data = json.dumps(data,ensure_ascii=False,indent=4)
print(export_data)

url = "https://api.aiforthai.in.th/ssense"
 
text = title
 
data = {'text':text}
 
headers = {
    'Apikey': "07IC7nlLNGUsFXcERk4PoBCoL9TW7u6s"
    }
 
response = requests.post(url, data=data, headers=headers)
sentiment_data = response.json()
# print(sentiment_data["sentiment"])

# print(response.json())