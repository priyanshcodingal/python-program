weight =int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))
bmi = weight / (height/100)**2
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.9:
    print("You are obese")
elif bmi <= 39.9:
    print("You are severely obese")
else:
    print("You need to go to a doctor")

