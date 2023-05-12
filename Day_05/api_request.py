import requests

response = requests.get("https://api.github.com/search/users?q=javascript")

print(response.json())
