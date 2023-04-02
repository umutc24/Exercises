

import requests
import json
url = "https://deckofcardsapi.com/api/deck/hvmenrzu5o66/draw/?count=3"

payload={}
headers = {
  'deck_id': 'hvmenrzu5o66'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

json_response = json.loads(response.text)
print(json.dumps(json_response, sort_keys=True, indent=4))
