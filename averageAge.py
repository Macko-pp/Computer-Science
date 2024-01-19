peopleNum = int(input("Ammount of people in class: "))
counter = 1
ages = []

while (counter <= peopleNum):
    studentAge = int(input(f"Student {counter} age: "))
    ages.append(studentAge)
    counter += 1

counter2 = 0
agesSum = 0

while (counter2 < len(ages)):
    agesSum += ages[counter2]
    counter2 += 1

averageAge = agesSum / len(ages)
print(f"\n{averageAge}")