import csv

with open('out.csv', 'r') as file:
    reader = csv.reader(file)
    array=[]
    for row in reader:
        array.append(row)
for item in array:
    print(item[0])