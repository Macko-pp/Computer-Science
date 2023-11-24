from math import sqrt

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print("")

def toInt(answer):
    if str(answer).endswith('.0'):
        return int(answer)
    else:
        return answer

slope = (y2 - y1)/(x2 - x1)
dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
mid = f"({toInt((x1 + x2) / 2)}, {toInt((y1 + y2) / 2)})"

def isNegative(num):
    if num < 0:
        return "-"
    else:
        return "+"

if isNegative(slope) == "-":
    yInt = y1 - (slope * x1)
else:
    yInt = y1 + (slope * x1)


equation = f"y = {toInt(slope)}x {isNegative(yInt)} {toInt(yInt)}"

print(f"Slope: {toInt(slope)}")
print(f"Distance: {toInt(dist)}")
print(f"Midpoint: {mid}")
print("")
print(toInt(yInt))
print(equation)