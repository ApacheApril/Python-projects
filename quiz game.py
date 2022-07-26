print("Welcome to my world quiz!")

playing = input("Do you want to start? ")

if playing != "yes":
    quit()
    
print("Let's start!")

answer = input("What country has the highest population? ")
if answer == "china" or "China":
    print("Correct!")
else:
    print("You lose.")

answer = input("What country is the oldest in the world? ")
if answer == "san marino" or "San marino":
    print("Correct!")
else:
    print("You lose.")

answer = input("What country is the least visited? ")
if answer == "Tuvalu" or "tuvalu":
    print("Correct!")
else:
    print("You lose.")

answer = input("What country is the most visited? ")
if answer == "France" or "france":
    print("Correct!")
else:
    print("You lose.")
    
answer = input("What country is the biggest? ")
if answer == "Russia" or "russia":
    print("Correct!")
else:
    print("You lose.")
    
answer = input("What country has the lowest GDP? ")
if answer == "Burundi" or "burundi":
    print("Correct!")
else:
    print("You lose.")
    
answer = input("What country has the highest GDP? ")
if answer == "United states" or "USA" or "united states" or "usa":
    print("Correct!")
else:
    print("You lose.")
    
answer = input("What is the tallesy statue? ")
if answer == "Statue of unity" or "statue of unity":
    print("Correct!")
else:
    print("You lose.")
    
answer = input("What country is the coldest? ")
if answer == "Canada" or "canaa":
    print("Correct!")
else:
    print("You lose.")

answer = input("What is North koreas full name ")
if answer == "Democratic people's republic of korea" or "democratic people's republic of korea" or "democratic peoples republic of korea":
    print("Correct!")
else:
    print("You lose.")
    
if answer != "Correct!":
    print("Congratulations, you win!")
    quit()