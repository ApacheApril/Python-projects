import random

player_wins = 0
AI_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock, Paper or Scissors! Press Q to cancel: ").lower()
    if user_input == "q":
        print("Bye!")
        quit()
    
    if user_input not in options:
        print("Please choose a valid option.")
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    AI_pick = options[random_number]
    print("Computer picked", AI_pick + ".")
    
    if user_input == "rock" and AI_pick == "scissors":
        print("You win!")
        player_wins += 1
        
    elif user_input == "paper" and AI_pick == "rock":
        print("You win!")
        player_wins += 1
        
    elif user_input == "scissors" and AI_pick == "paper":
        print("You win!")
        player_wins += 1
        
    elif user_input == AI_pick:
        print("You drawed!")    
        
    else:
        print("You lose!")
        AI_wins += 1
        
        
        
print("You won", player_wins, "times!")
print("The computer won", AI_wins, "times!")
    
    
    
    
    
    
    
    