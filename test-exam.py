age = int(input("Age:"))

if age >= 16 and age <= 20:
    grade1 = float(input("Grade 1:"))
    grade2 = float(input("Grade 2:"))
    grade3 = float(input("Grade 3:"))
    average = (grade1 + grade2 + grade3) / 3
    tuition = float(input("Tuition: "))
    
    if average >= 3.5 and average <= 3.8:
        print("You have been granted 30% of the value of the following semester 🟠")
        dTuition = tuition - ((30 / 100) * tuition)
        print(f"The tuition was {tuition}, it is now {dTuition}")

    elif average >= 3.9 and average <= 4.2:
        print("You have been granted 40% of the value of the following semester 🟡")
        dTuition = tuition - ((40 / 100) * tuition)
        print(f"The tuition was {tuition}, it is now {dTuition}")

    elif average >= 4.3 and average <= 4.6:
        print("You have been granted 50% of the value of the following semester 🟡")
        dTuition = tuition - ((50 / 100) * tuition)
        print(f"The tuition was {tuition}, it is now {dTuition}")

    elif average >= 4.6 and average <= 5.0:
        print("You have been granted 100% of the value of the following semester 🟢")
        dTuition = tuition - ((100 / 100) * tuition)
        print(f"The tuition was {tuition}, it is now {dTuition}")

    else:
        print("No grant for you! 🔴")
else:
    print("You are not elegible 🔴")