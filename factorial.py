factorialInput = int(input("Factorial: "))
factorial = 1

# Validation to ensure no negative numbers
while (factorialInput <= 0):
    print("Please input a positive natural number")
    factorialInput = int(input("Factorial: "))

# Calculate factorial
for i in range(1, factorialInput+1):
    factorial *= i

print(factorial)