import csv

with open("students.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Anjali", 19])
    writer.writerow(["Priya", 20])

print("Data saved successfully!")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


