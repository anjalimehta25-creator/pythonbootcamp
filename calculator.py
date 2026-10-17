try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter valid numbers.")

except ZeroDivisionError:
    print("Error! You cannot divide by zero.")

finally:
    print("Thank you for using the calculator!")