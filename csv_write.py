import csv

write_csv = [
    [9, "David Miller", 39, "Marketing", 85000],
    [10, "Laura Johnson", 41, "HR", 60000],  
    [11, "James Anderson", 26, "Sales", 20000] 
]

with open('csv_write.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(write_csv)
    print(write_csv)

