import requests

BASE = "http://127.0.0.1:8080/"
url = "https://medium.com/@saitarn14/ติดตั้ง-python-flask-framework-สำหรับทำ-web-application-ด้วย-virtual-environments-7d5235687b2d"
response = requests.get(BASE + "connect")
print(response.json())