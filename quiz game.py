print("Welcome to my world quiz!")

playing = input("Do you want to start? ")

if playing.lower() != "yes":
    quit()
    
print("Let's start!")
score = 0

answer = input("What country has the highest population? ")
if answer.lower() == "china": 
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer2 = input("What country is the oldest in the world? ")
if answer2.lower() == "san marino":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer3 = input("What country is the least visited? ")
if answer3.lower() == "tuvalu":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer4 = input("What country is the most visited? ")
if answer4.lower() == "france":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
    
answer5 = input("What country is the biggest? ")
if answer5.lower() == "russia":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
    
answer6 = input("What country has the lowest GDP? ")
if answer6.lower() == "burundi":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer7 = input("What country has the highest GDP? ")
if answer7.lower() == "united states of america":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer8 = input("What is the tallest statue? ")
if answer8.lower() == "statue of unity":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer9 = input("What country is the coldest? ")
if answer9.lower() == "canada":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")

answer0 = input("What is North koreas full name? ")
if answer0.lower() == "democratic peoples republic of korea":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
if answer != "Correct!":
    print("Congratulations, you got " + str(score) + " questions correct!")
    quit()