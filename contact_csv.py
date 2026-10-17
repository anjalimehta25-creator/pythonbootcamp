import csv

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].startswith("A"):
            print(row)