import csv
filename = open('indians-diabetes.data.csv', 'r')
reader = csv.reader(filename, delimiter=',')
lines = list(reader)
print("\n\n No of rows:", len(lines), "\n\n")
print(lines)
print("\n\n")
for l in lines :
    print(l)