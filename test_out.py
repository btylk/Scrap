from lxml import html
import codecs
import requests

file=codecs.open('fb3.txt','w+','utf-8')
try:
    page = requests.get('https://www.jeban.com/topic/118684')
except:
    file.close()
tree = html.fromstring(page.content)
q = tree.xpath('//*/text()')
for data in q:
    if not data.isspace():
        file.write(data+'\n')
