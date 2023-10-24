from random import randint

myValue = int(input("Type an int between 1 and 20: "))
compValue = randint(1, 20)

print(f"My Value: {myValue}")
print(f"Comp Value: {compValue}")

if myValue > compValue:
    print("I win!")

elif myValue < compValue:
    print("The computer wins")

else:
    print("It's a tie")