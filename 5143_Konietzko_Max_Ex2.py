# Import only the required function
from random import randint

# Play the game forever unless the user ends it instead of running it everyy time
while True:
    # get and analyze the computers play
    comPlay = randint(1, 3)

    if comPlay == 1:
        comPlay = "R"
    elif comPlay == 2:
        comPlay = "P"
    else:
        comPlay = "S"

    # get the users play
    userPlay = input("Enter your play: ")

    # check if the user ends the game by typing "end" into their play
    if userPlay == "end":
        print("\n-------------------------------------------------------------------------------\n")
        break

    # checking for invelid characters apart from "R", "P", "S", and "end" (for redundancy)
    if userPlay != "R" and userPlay != "P" and userPlay != "S" and userPlay != "end":
        print("That is not a valid play, please input 'R', 'P', or 'S'\n")
        continue

    # showing the users and the computers play
    print(f"User's play {userPlay}")
    print(f"Computer's play {comPlay}")
    print("-------------------------------------------------------------------------------")

    # User wins
    if userPlay == comPlay:
        print("Its a tie, nobody wins!")
    elif userPlay == "R" and comPlay == "S":
        print("Rock crushes Scissors, You WIN !!!")
    elif userPlay == "P" and comPlay == "R":
        print("Paper wraps around Rock, You WIN !!!")
    elif userPlay == "S" and comPlay == "P":
        print("Scissors cut Paper, You WIN !!!")

    # Computer wins
    elif comPlay == "R" and userPlay == "S":
        print("Rock crushes Scissors, the computer WINS !!!")
    elif comPlay == "P" and userPlay == "R":
        print("Paper wraps around Rock, the computer WINS !!!")
    elif comPlay == "S" and userPlay == "P":
        print("Scissors cut Paper, the computer WINS !!!")

    print("*** GAME OVER ***\n")

# Made by Max Konietzko, 10R, Oct 24, 2023