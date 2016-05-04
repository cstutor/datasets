import csv

with open('vashon-hills.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print row
