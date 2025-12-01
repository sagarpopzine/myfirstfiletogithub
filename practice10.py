weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in meters: "))
bmi=round(weight/height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} and you have underweight")
elif bmi < 25:
     print(f"your bmi is {bmi} and you have normalweight")
elif bmi < 30:
     print(f"your bmi is {bmi} and you have overweight")
elif bmi < 35:
     print(f"your bmi is {bmi} and you have obese")
else:
     print("you have to go for clinic to check your obese")