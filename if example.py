import random
drinks = ("tequila", "vodka", "rum", "gin", "wine", "fernet")
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age) # convert string to integer
    country = input("Where are you from? ")
except ValueError:
    print("Invalid age. Please entre a number")
else:
    if age < 0 or age > 140:
        print("You are not human. You can't play the awesome drinking game")
    elif age > 120:
        print("You are too old. You can't play the awesome drinking game")
    elif age < 18:
        print("You are a minor. You can't play the awesome drinking game")
    elif country == "USA" or country == "UAE" and age < 21:
        print("You are not allowed to drink in USA or UAE. You can't play the awesome drinking game")
    else:
        print("You are an adult. You can play the awesome drinking game")
        print("Have some", random.choice(drinks), "and enjoy the game")