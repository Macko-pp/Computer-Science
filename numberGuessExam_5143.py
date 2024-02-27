from random import randint

while True:
    randNum = randint(1, 50)
    gotIt = False

    for i in range(3):
        guess = int(input("\nEnter a number between 1 and 50: "))
        print("")
        if (guess != randNum):
            if (abs(guess - randNum) >= 20):
                print("You're freezing cold!")
            elif (abs(guess - randNum) < 20 and abs(guess - randNum) > 10):
                print("You're getting warmer!")
            else:
                print("You're hot on the trail!")
            
            if (guess > randNum):
                print("You overshot!")
            else:
                print("You undershot!")
        
        else:
            print("Congrats! You guessed the secret number!")
            gotIt = True
            break
    if (gotIt == False):
        print("\nYou ran out of attempts :(")
        print("The secret number was ", randNum)
    
    again = input("Would you like to play again? (y/n): ")
    if (again == "n"):
        break
