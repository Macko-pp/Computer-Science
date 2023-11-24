weight = float(input("Weight: "))
height = float(input("Height: "))

def toInt(answer):
    if str(answer).endswith('.0'):
        return int(answer)
    else:
        return answer

BMI = weight/height**2
print(toInt(BMI))
