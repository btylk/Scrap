from lxml import html
import codecs
import requests

file=codecs.open('./data/droidsan.txt','w+','utf-8')
try:
    page = requests.get('https://droidsans.com/oneplus-nord-n10-5g-line-friends-special-box-set-announced/')
except:
    file.close()
tree = html.fromstring(page.content)
q = tree.xpath('//*/text()')
for data in q:
    if not data.isspace():
        file.write(data+'\n')
