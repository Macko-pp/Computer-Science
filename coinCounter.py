excess = 0
a200 = 0
a500 = 0
a1000 = 0
coinAmmount = int(input('Enter amont of coins: '))

for i in range(coinAmmount + excess):
    # weight = float(input("Coin Weight: "))
    diameter = float(input("Coin Diameter: "))

    # if (weight == 4.6 and diameter == 22.3):
    if (diameter == 22.3):
        a200 += 1

    # elif (weight == 7.45 and diameter == 24.55):
    elif (diameter == 24.55):
        a500 += 1

    # elif(weight == 9.72 and diameter == 26.5):
    elif(diameter == 26.5):
        a1000 += 1

    else:
        print("Not a Valid Coin")
        excess += 1
        continue

    print(f'''
    ┌─────────────────┐
    │ 200: {a200}          │
    │ 500: {a500}          │
    │ 1000: {a1000}         │
    │ Total: {a200 * 200 + a500 * 500 + a1000 * 1000}     │
    └─────────────────┘
        ''')