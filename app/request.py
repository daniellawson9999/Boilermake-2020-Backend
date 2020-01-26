import requests 
import re
import json

url = 'https://nypost.com/2020/01/25/china-steps-up-fight-against-deadly-coronavirus-outbreak/'
API_ENDPOINT = "https://api.diffbot.com/v3/article"

ttl = {'token':'3e30c795c4208bafafb20aec78f9ccc1',
         'url':  url}

r = requests.get(API_ENDPOINT, params = ttl) 
api_response = r.content
title1 = json.loads(api_response)["objects"][0]["title"]
author1 = json.loads(api_response)["objects"][0]["author"]
txt = json.loads(api_response)["objects"][0]["text"]

print(title1)
print(author1)
print(txt)