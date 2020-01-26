import requests 
import re
import json

url = 'https://nypost.com/2020/01/25/china-steps-up-fight-against-deadly-coronavirus-outbreak/'

param = {'token':'3e30c795c4208bafafb20aec78f9ccc1',
           'url':  url}
API_ENDPOINT = "https://api.diffbot.com/v3/article"
r = requests.get('https://api.diffbot.com/v3/article', params = param) 
api_response = r.content

formatted = json.loads(api_response)["objects"][0]["html"]
clean = re.sub(r'<.+?>', '', formatted)
print(clean)
