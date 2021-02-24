import random

user_score = 0
computer_score = 0

rps = ["rock", "paper", "scissors"]

while True:
    user_rps = input("What do you choose, rock, paper or scissors or q to quit?")
    if user_rps == "q":
        print(f"Overall you scored {user_score} and the computer scored {computer_score}.")
        print("You have quit.")
        break

    computer_rps = rps[random.randint(0, 2)]
    print("The computer chose " + computer_rps)
    if user_rps == computer_rps:
        print("You and the computer both picked the same.")

    elif user_rps == "rock":
        if computer_rps == "scissors":
            print("You have beaten the computer, well done")
            user_score += 1
        elif computer_rps == "paper":
            print("You have been beaten by the computer, better luck next time.")
            computer_score += 1

    elif user_rps == "paper":
        if computer_rps == "rock":
            print("You have beaten the computer, well done")
            user_score += 1
        elif computer_rps == "scissors":
            print("You have been beaten by the computer, better luck next time.")
            computer_score += 1

    elif user_rps == "scissors":
        if computer_rps == "paper":
            print("You have beaten the computer, well done")
            user_score += 1
        elif computer_rps == "rock":
            print("You have been beaten by the computer, better luck next time.")
            computer_score += 1

    else:
        print("Invalid input.")


