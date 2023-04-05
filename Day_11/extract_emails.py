import requests

import re




url = "https://cleantalk.org/blacklists/ivanov@gmail.com"

html = requests.get(url).text

result = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", html)

print(result)
