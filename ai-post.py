import requests
 
url = "https://api.aiforthai.in.th/bully"
 
text = 'รกโลก'
 
data = {'text':text}
 
headers = {
    'Apikey': "07IC7nlLNGUsFXcERk4PoBCoL9TW7u6s",
    }
 
response = requests.post(url, data=data, headers=headers)
 
print(response.json())