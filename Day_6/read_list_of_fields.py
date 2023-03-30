import json
import requests

response = requests.get("https://api.github.com/search/users?q=javascript")

json_data=response.json()

usersCount = len(json_data['items'])-1

for x in range(usersCount):
    print (json_data['items'][x]['html_url'])
