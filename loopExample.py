number = int(input("Type the ammount of natural numbers: "))

for i in range(1, number + 1):
    print(i)

print("")

for i in range(1, number + 1):
    if i % 2 == 1:
        print(i)

print("")

for i in range(1, number * 2 + 1):
    if i % 2 == 0:
        print(f"1/{i}")

