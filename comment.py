import codecs
from lxml import html
import requests
file=codecs.open('./data/bn-commnet.txt','w+','utf-8')
try:
    page = requests.get('https://www.blognone.com/node/120115')
except:
    file.close()
tree = html.fromstring(page.content)
q = tree.xpath('//*/div[2]/div[2]/div/div/div/p/text()')
for data in q:
    if not data.isspace():
        file.write(data+'\n')