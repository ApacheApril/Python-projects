import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("That number is to small.")
        quit()
else:
    print("Type a number next time.")

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1 
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a number next time.")
        continue
    
    if guess == random_number:
        print("You win!")
        break
    
    elif guess > random_number:
        print("You guessed above the number.")
    else:
        print("You guessed below the number.")
        
        
print("You guessed the number in", guesses, "tries!")
                
    

