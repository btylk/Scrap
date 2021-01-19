import requests

url = "http://127.0.0.1:8080/test_post"

payload={'input_value': 'https://stackoverflow.com/questions/42011100/how-can-i-pass-post-parameters-in-fetch-request-react-native'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.json())