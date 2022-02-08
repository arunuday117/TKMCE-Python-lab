import csv

with open('class.csv') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
