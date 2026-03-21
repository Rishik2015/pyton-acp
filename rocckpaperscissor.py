import random
print("Welcome to rock,paper,scissors\n")
player__wins = 0
computer__wins = 0
while True:
    player = input("enter a choice(rock paper scissors)")
    choices = ["rock","paper",  "scissors"]
    computer = random.choice(choices)
    print(f"\nyou chose {player} ,computer chose {computer}")
    if player == computer:
        print(f"both players selected{player}.it is a tie")
    elif player == "rock":
        if computer == "scissors":
            print("rock smashes scissors. you Win")
            player__wins+=1

        else:
            print("paper covers rock .you lose")     
            computer__wins+=1
    elif player == "paper":
        if computer == "rock":
            print("paper covers rock.you win")
            player__wins+=1
        else:
            print("scissors cut paper.you lose" )  
            computer__wins+=1  
    elif player == "scissors":
        if computer == "paper":
            print("scissors cut paper.you win .")
            player__wins+=1
        else:
            print("rock smashes scissors.you lose" )  
            computer__wins+=1   
    print("You have "+str(player__wins)+" wins")

    print("The computer has "+str(computer__wins)+" wins")

    repeat = input("\nPlay again? (yes/no): ")

    if repeat.lower() != "yes":

        print("Thanks for playing!")
    break               