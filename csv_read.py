import csv

csv_file = open('text.csv', 'r') 
with csv_file:
    read_csv = csv.reader(csv_file)
    for row in read_csv:
        print(row)

