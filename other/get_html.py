import requests

r = requests.get('https://www.blognone.com/node/119064')
with open('./data/html.txt','wb') as f:
    f.write(r.content)