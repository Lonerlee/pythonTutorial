import csv

file = open('NewCSVFile.csv')
szukacz = csv.reader(file)

print("Shows all values of the CSV file:")

for line in szukacz:
    print(line)

print("Shows every single column name:")

with open("NewCSVFile.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    nameOfData = reader.fieldnames
    print(nameOfData)