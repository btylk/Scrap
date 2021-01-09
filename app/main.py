#Server side

from flask import Flask, request
from flask_restful import Api, Resource
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
api = Api(app)

class testResource(Resource):
    def get(self):
        url = "https://www.msn.com/th-th/news/national/ข่าวดีแรงงาน-ประกันสังคมแจ้งผู้รับผลกระทบโควิด-ยื่นรับสิทธิว่างงาน-ดีเดย์-4-มกราคมนี้/ar-BB1cqX4N"
        res = requests.get(url)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html5lib')
        title = soup.title.string
        h1 = soup.h1.string
        if h1 != title:
            pass
        else:
            h1 = None
        h2 = soup.h2.string
        return {"title": title, "h1": h1}

api.add_resource(testResource, "/connect")

if __name__ == "__main__":
    app.run(debug=True, port=8080)