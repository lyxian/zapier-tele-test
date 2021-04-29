from main import getToken
import requests
import json

token = getToken()

method_name = r'sendMessage'
#`method_name = r'getMe'

chat_id = 1787632790
#chat_id = 315498839

payload = {
    'chat_id': str(chat_id), 
    'text': '/hello'
}

url = "https://api.telegram.org/bot{0}/{1}".format(token, method_name)

#msg = requests.get(url).json()
msg = requests.post(url, json=payload).json()

print(msg)
