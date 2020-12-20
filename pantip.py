import codecs
from lxml import html
import requests
file=codecs.open('./data/pantip-commnet.txt','w+','utf-8')
try:
    page = requests.get('https://pantip.com/topic/40386446')
except:
    file.close()
tree = html.fromstring(page.content)
q = tree.xpath('//*/div/div[2]/div[2]/div/text()')
for data in q:
    if not data.isspace():
        file.write(data+'\n')