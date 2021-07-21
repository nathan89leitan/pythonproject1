import random
randomnumber = random.randint(1,9)
chances = 0
number=randomnumber
while chances < 5:
    guess=int(input("enter your guess if you dare "))
    if guess == number:
        print("YOU WIN!!!")
        break
    elif not chances < 5:
        print("YOU LOSE!!! The Number is " + number)