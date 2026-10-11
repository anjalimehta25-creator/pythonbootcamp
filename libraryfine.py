book_type = input("Enter book type (standard/reference): ")
days = int(input("Enter overdue days: "))
premium = input("Are you a premium member? (yes/no): ")

if days <= 0:
    fine = 0
elif book_type == "standard":
    if days <= 5:
        fine = days * 5
    else:
        fine = (5 * 5) + ((days - 5) * 10)
elif book_type == "reference":
    fine = days * 20
else:
    print("Invalid book type")
    exit()

if premium == "yes":
    fine = fine * 0.80

print("Total library fine: Rs.", fine)