import csv

csv_file = open('test.csv', 'w')

writer = csv.writer(csv_file, delimiter =';')

header = ['Last name', 'First name', 'Age', 'Country']

data = ['Smith', 'John', '35', 'USA']

writer.writerow(header)

writer.writerow(data)

csv_file.close()
