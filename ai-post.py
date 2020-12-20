import requests
 
url = "https://api.aiforthai.in.th/bully"
 
text = 'เสร่อ'
 
data = {'text':text}
 
headers = {
    'Apikey': "07IC7nlLNGUsFXcERk4PoBCoL9TW7u6s",
    }
 
response = requests.post(url, data=data, headers=headers)
 
print(response.json())