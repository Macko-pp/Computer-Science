from math import sqrt

latA = int(input("latA: "))
longA = int(input("longA: "))

latB = int(input("latB: "))
longB = int(input("longB: "))

distance = sqrt((latA - latB)**2 + (longA - longB)**2)
print(str(distance) + "km")

if distance > 50 and distance <= 1000:
    print("DR1000 selected")
    print("Target Reached, we did it boys 👍")
elif distance > 1000 and distance <= 3500:
    print("DR2000 selected")
    print("Target Reached, we did it boys 👍")
elif distance > 3500 and distance <= 7000:
    print("DR3000 selected")
    print("Target Reached, we did it boys 👍")
else:
    print("No drone is suitable for this operation 😥 no bombing today boys")