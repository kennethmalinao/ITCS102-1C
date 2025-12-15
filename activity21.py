import random

print("NUMBER GUESSING GAME")
print("********************************")

random_value = random.randint(1,3)
tries = 0
tuloy = True

name = input("What's your name? ").title()
print("HI!", name)

while tuloy == True:
    num = int(input("Guess a number from 1 to 20: "))

    if num == random_value:
        tries += 1
        print("Congratulations!!!!", name) 
        print(f"Good job {name} Your Guess is Correct, Number of Tries", tries)
        break
    else:
        print("Incorrect Guess") 

        continue    