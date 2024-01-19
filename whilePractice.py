x = int(input("X: "))
y = int(input("Y: "))

while (x >= y):
    print("X is larger than Y or X is the same as Y, please make Y larger than X.")
    x = int(input("X: "))
    y = int(input("Y: "))

lc = x

while (lc <= y):
    if (lc % 2 == 0):
        print(lc)

    lc = lc + 1

print("\nDONE")
