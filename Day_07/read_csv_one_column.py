import csv

with open("test.csv", 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader: 
    columns=row[0].split(";")
    print(columns[0])
