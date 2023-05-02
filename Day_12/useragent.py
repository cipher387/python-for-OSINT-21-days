import requests

url = 'https://www.whatismybrowser.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response.text)
