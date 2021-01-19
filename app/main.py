#Server side

from flask import Flask, request
from flask import jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)
api = Api(app)
CORS(app)
# class testResource(Resource):
#     def get(self):
#         url = "https://www.msn.com/th-th/news/national/ข่าวดีแรงงาน-ประกันสังคมแจ้งผู้รับผลกระทบโควิด-ยื่นรับสิทธิว่างงาน-ดีเดย์-4-มกราคมนี้/ar-BB1cqX4N"
#         res = requests.get(url)
#         res.encoding = "utf-8"
#         soup = BeautifulSoup(res.text, 'html5lib')
#         title = soup.title.string
#         h1 = soup.h1.string
#         if h1 != title:
#             pass
#         else:
#             h1 = None
#         h2 = soup.h2.string
#         data = {'Data':[{'Title': title, 'H1': h1, 'H2': h2}]}
#         export_data = json.dumps(data,ensure_ascii=False,indent=4)
#         # print(export_data)
#         return export_data

# api.add_resource(testResource, "/connect")

@app.route('/my_json', methods=['GET'])
def my_json():
	if request.method == 'GET':
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
		data = {
			'Title': title,
			'H1': h1
		}						
		return jsonify(data)
	return '200'
@app.route('/test_post', methods=['POST','GET'])
def test_post():
	if request.method == 'POST':
		# input_value = request.form["input_value"]
		# url = input_value
		req = request.get_json()
		url = req['data']
		# # url = req*5
		# # url = data
		res = requests.get(url)
		res.encoding = "utf-8"
		soup = BeautifulSoup(res.text, 'html5lib')
		title = soup.title.string
		return jsonify(title)
		# return jsonify(req)
	if request.method == 'GET':
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
		data = {
			'Title': title,
			'H1': h1
		}
		return jsonify(data)
	return '200'

if __name__ == "__main__":
    app.run(debug=True, port=8080)