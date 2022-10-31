from private import api_key 
import requests
url = "https://api.trint.com/export/srt/RDOnOc0pRpaJ89CuBP3beA?captions-by-paragraph=false&max-subtitle-character-length=37&highlights-only=false&enable-speakers=false&speaker-on-new-line=false&speaker-uppercase=false&skip-strikethroughs=false"
headers = {
    "accept": "application/json",
    "api-key": api_key,
    }
response = requests.get(url, headers=headers)
url = response.json()['url']
data = requests.get(url)
import pdb;pdb.set_trace()
print(response.text)
