import requests
from private import api_key

url = "https://upload.trint.com/?language=de&filename=Kurzpausen%20BG%20_%20Wolf%20_%20Bodyscan.mp3&detect-speaker-change=true&custom-dictionary=true"

with open('./tests/Kurzpausen+BG+_+Wolf+_+Bodyscan.mp3', 'rb') as f:
    data = f.read()

headers = {
    "accept": "application/json",
    "api-key": api_key,
    "content-type": "audio/mpeg"
    }


response = requests.post(url, headers=headers, data = data)

import pdb;pdb.set_trace()
print(response.text)
