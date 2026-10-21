from random import randint

dice1 = randint(1,6)
dice2 = randint(1,6)
sum = dice1 + dice2
if sum == 12:
    print("jackpot")
else:
    print(dice1,dice2)