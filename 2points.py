# Import the sqrt function from the math module
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# Get user input for x1, y1, x2, y2
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print("")

# Define a function to convert float answers to integers
def toInt(answer):
    # Check if the answer ends with '.0'
    if str(answer).endswith('.0'):
        # Convert to integer to remove the .0
        return int(answer)
    else:
        # Otherwise, round the answer to 2 decimal places
        return round(answer, 2)

# Calculate the slope, distance, and midpoint
slope = (y2 - y1)/(x2 - x1)
dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
mid = f"({toInt((x1 + x2) / 2)}, {toInt((y1 + y2) / 2)})"

# Define a function to determine if a number is negative
def isNegative(num):
    # Check if the number is less than 0
    if num < 0:
        return "-"
    else:
        return "+"

# Calculate the y-intercept
if isNegative(slope) == "-":
    yInt = y1 - (slope * x1)
else:
    yInt = y1 + (slope * x1)

# Create the equation string
equation = f"y = {toInt(slope)}x {isNegative(yInt)} {toInt(yInt)}"

# Print the results
print(f"Slope: {toInt(slope)}")
print(f"Distance: {toInt(dist)}")
print(f"Midpoint: {mid}")
print("")
print(f"y Intercept: {toInt(yInt)}")
print(equation)

#-------------------------------------------------------------------------------

x = np.array([x1, x2])
y = np.array([y1, y2])

plt.plot(x,y)
plt.show()