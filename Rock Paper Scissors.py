import random

print("Welcome to Rock, Paper, or Scissors")
print("Please enter: rock, paper, scissors, or quit")
choice = ["rock", "paper", "scissors"]
player_point = 0
comp_point = 0
    
while True:
        
        comp = random.choice(choice)
        player = input("Enter your choice: ").lower()
        
        
        if player == "quit":
            print("Thank you for playing")
            break
        
        if player not in choice:
            print("Invalid choice. Please pick rock, paper, scissors, or quit")
            continue
        
        print(f"Computer Picks, {comp}")
        
        if player == "rock" and comp == "scissors":
            player_point += 1
            print("Player point:",player_point)
        
        elif player == "scissors" and comp == "paper":
            player_point += 1
            print("Player point:",player_point)
        
        elif player == "paper" and comp == "rock":
            player_point += 1
            print("Player point:",player_point)
        
        elif player == "paper" and comp == "scissors":
            comp_point += 1
            print("Computer point:",comp_point)
        
        elif player == "scissors" and comp == "rock":
            comp_point += 1
            print("Computer point:",comp_point)
        
        elif player == "rock" and comp == "paper":
            comp_point += 1
            print("Computer point:",comp_point)
            
        if player_point == 3 or comp_point == 3:
            break
if player_point > comp_point:
        print("Player Wins")
else:
        print("Computer Wins")
        
