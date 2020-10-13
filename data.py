from lxml import html
import codecs
import requests
i=0
d=True
file=codecs.open('./data/data2.txt','w+','utf-8')
while d==True:
    try:
        page = requests.get('https://www.blognone.com/node?page='+str(i))
    except:
        file.close()
        d=False
        break
    tree = html.fromstring(page.content)
    q = tree.xpath('//h2[@itemprop="name"]/a/text()')
    for data in q:
        file.write(data+'\n')
    i+=1

# ดึงจากทุกเพจของ blognone