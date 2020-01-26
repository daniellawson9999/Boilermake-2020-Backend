import requests 
import re
import json

url = 'https://www.bbc.com/news/world-us-canada-51253066'
API_ENDPOINT = "https://api.diffbot.com/v3/article"

ttl = {'token':'3e30c795c4208bafafb20aec78f9ccc1',
         'url':  url}

r = requests.get(API_ENDPOINT, params = ttl) 
api_response = r.content

try:
    title1 = json.loads(api_response)['objects'][0]['title']
except:
    title1 = 'no title found'

try:
    author1 = json.loads(api_response)['objects'][0]['author']
except:
    author1 = 'no author found'

txt = json.loads(api_response)['objects'][0]['text']
print(title1)
print(author1)
print(txt)