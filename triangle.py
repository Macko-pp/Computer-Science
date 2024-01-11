side1 = int(input("Side1: "))
side2 = int(input("Side2: "))
side3 = int(input("Side3: "))

square_side1 = side1 ** 2
square_side2 = side2 ** 2
square_side3 = side3 ** 2

print("-------------------------------------------------------------------------------\n")

print("Report:")
print(f"Side 1: {side1}")
print(f"Side 2: {side2}")
print(f"Side 3: {side3}")

if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    print("Triangle Exists")

    if (side1 == side2 == side3):
        print("Triangle is equilateral")

    elif ((side1 == side2) or (side2 == side3) or (side3 == side1)):
        print("Triangle is isosceles")

    else:
        print("Triangle is scalene")

else:
    print("Triangle does not exist")
