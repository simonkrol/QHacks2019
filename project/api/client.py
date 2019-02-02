import json
import requests
from flask import send_file

#my file to be sent
local_file_to_send = '../../input/Train/train/4.wav'

url = "http://127.0.0.1:5000/customerupdate"

files = [

    ('document', (local_file_to_send, open(local_file_to_send, 'rb'), 'audio/wav' ))
]


r = requests.post(url, files=files)
print(str(r.content, 'utf-8'))
