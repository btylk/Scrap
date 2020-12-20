import requests
 
url = "https://api.aiforthai.in.th/bully"
 
text = 'ฆ่า'
 
params = {'text':text}
 
headers = {
    'Apikey': "07IC7nlLNGUsFXcERk4PoBCoL9TW7u6s"
    }
 
response = requests.get(url, headers=headers, params=params)
 
print(response.json())