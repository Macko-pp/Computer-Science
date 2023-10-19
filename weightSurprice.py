basePrice = 10000
weight = int(input("Weight: "))
surPrice = 0

if weight < 15:
    print("No Shipping Fee")
    print(f"Final Price: {basePrice}")

elif weight >= 15 and weight <= 20:
    surPrice = 15000
    finalPrice = basePrice + surPrice
    print(f"Shipping Fee: {surPrice}")
    print(f"Final Price: {finalPrice}")

elif weight > 20:
    surPrice = 20000
    finalPrice = basePrice + surPrice
    print(f"Shipping Fee: {surPrice}")
    print(f"Final Price: {finalPrice}")