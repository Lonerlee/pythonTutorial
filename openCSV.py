import csv

file = open('NewCSVFile.csv')
szukacz = csv.reader(file)

for line in szukacz:
    print(line)