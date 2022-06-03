import random

print("Welcome toRock, Papper, Sciccors")

user_score = 0
cpu_score = 0

while True:
    print()
    user_choice = input("Rock, Papper, or Sciccors")
    while user_choice != "rock" and user_choice != "papper" and user_choice != "sciccors":
        user_choice = input("invalid input, please try again:")

    random_num = random.randint(1, 3)
    if random_num == 1:
        cpu_choice = "rock"
    elif random_num == 2:
         cpu_choice = "papper"
    elif random_num == 3:
         cpu_choice = "sciccors"

    print()
    print("your choice:", user_choice)
    print("computers choice:", cpu_choice)
    print()

    if user_choice == "rock":
        if cpu_choice == "rock":
            print("its a tie")
        elif cpu_choice == "papper":
             print("you lost!")
             user_score += 1
        elif cpu_choice == "sciccors":
             print("you win")
             user_score += 1
    elif user_choice == "papper":
        if cpu_choice == "papper":
            print ("its a tie!")
        elif cpu_choice == "sciccors":
             print("you lost!")
             cpu_score += 1
        elif cpu_choice == "rock":
             print("you win!") 
             cpu_score += 1
    elif user_choice == " sciccors":
        if cpu_choice == "sciccors":
             print("its a tie!") 
        elif cpu_choice == "rock":
             print("you lost!")
             cpu_score += 1       
        elif cpu_choice == "papper":
            print("you win!")
            user_score += 1

    print("You have", user_score, "wins")
    print("The computer has", cpu_score, "wins")
    print()

    repeat = input("play Again? (Y/N").lower()  
    while repeat != "n" and repeat != "y":
        repeat = input("Invalid input, please try again:").lower()    

    if repeat == "n": 
        break 


    print("/n---------------------------------\n")           




