packagesNum = int(input("Number of packages: "))

priceSum = 0

lc = 1
while (lc <= packagesNum):
    packageWeight = int(input(f"Weight of package No. {lc}: "))

    if (packageWeight > 15 and packageWeight <= 20):
        surcharge = 15000

    elif (packageWeight > 20.1):
        surcharge = 20000

    else:
        surcharge = 0

    shipPrice = 10000 + surcharge
    priceSum += shipPrice

    print(f"The shipping price for this package is ${shipPrice}")

    lc += 1

print(f"Total price for shipment of packages is ${priceSum}")