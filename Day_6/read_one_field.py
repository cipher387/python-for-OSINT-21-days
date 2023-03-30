import json
import requests

response = requests.get("https://api.github.com/search/users?q=javascript")

json_data=response.json()

print (json_data['total_count'])

print (json_data['items'][0]['html_url'])
