import random

lives = 3
while lives:
    print("You have ", lives, "lives left. ")
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    if dice == 6:
        print("You win! ")
        break
    lives -= 1
else:
    print("You lose! ")
print("Thank you for playing. Goodbye")
