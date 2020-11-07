import requests
url = 'https://titanreadchatbot.herokuapp.com/webhooks/rest/webhook'
obj = {
"message": "Hello",
"sender": "Atul",
}

x = requests.post(url, json=obj)
print(x.text)
