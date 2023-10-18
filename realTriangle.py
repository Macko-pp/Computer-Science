side1 = int(input("Side1: "))
side2 = int(input("Side2: "))
side3 = int(input("Side3: "))

if (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2:
    print("Triangle Exists")
else:
    print("Triangle does not exist")
