import json
import requests
import csv


response = requests.get("https://api.github.com/search/users?q=javascript")

json_data=response.json()


csv_file = open('test.csv', 'w')

writer = csv.writer(csv_file, delimiter =';')

usersCount = len(json_data['items'])-1

for x in range(usersCount):
    row = []
    row.append(json_data['items'][x]['login'])
    row.append(json_data['items'][x]['html_url'])
    row.append(json_data['items'][x]['avatar_url'])
    writer.writerow(row)
   

csv_file.close()





