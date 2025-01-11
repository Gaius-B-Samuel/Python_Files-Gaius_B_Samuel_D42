weight=float(input("Enter your weight in (kg): "))
height=float(input("Enter your height in (m): "))

bmi=weight/(height**2)
print("Your BMI is:",round(bmi,2))

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 25:
    category = "normal"
elif 25 <= bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(f"You are in the '{category}' range.")
