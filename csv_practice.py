import csv

with open("group_5_table.csv", mode = "r") as f:
    r = csv.DictReader(f)
    j = 0
    for row in r:
        i = 0
        for e in row:
            print(j)
            print(e)
            i += 1
        j += 1
