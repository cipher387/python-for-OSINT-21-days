import requests


proxies = {
  'https': '135.181.149.47:8080',
}


url = 'https://cleantalk.org/blacklists/ivanov@gmail.com'


response = requests.post(url, proxies=proxies)


print(response.text)
