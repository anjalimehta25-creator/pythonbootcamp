import random

computer_number = random.randint(1, 50)

for i in range(3):
    user_number = int(input("Enter the number: "))

    if user_number == computer_number:
        print("You win, congrats!")
        break
    else:
        print("Wrong guess, try again")

else:
    print("you attemps 3 , best luck for next time")
    print("the correct is:",computer_number)