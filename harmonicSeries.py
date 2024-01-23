lc = 1
la = 0

n = int(input("n: "))

while (lc <= n):
    la += 1 / lc ** 2
    print(f"1/{lc}²", end=" ")
    lc += 1

print("")
print(la)
print("\nDONE")
