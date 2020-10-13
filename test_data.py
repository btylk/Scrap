from lxml import html
import codecs
import requests
def get_data():
    file=codecs.open('fb2.txt','w+','utf-8')
    try:
        page = requests.get('https://www.blognone.com/node/118941')
    except:
        file.close()
    tree = html.fromstring(page.content)
    q = tree.xpath('//*/text()')
    for data in q:
        if not data.isspace():
            file.write(data+'\n')

# แบบดึงได้ทั้งหน้าแต่ติดโค๊ดมาด้วย
