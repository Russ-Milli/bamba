weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in metres:"))
bmi = weight/(height**2)
print(f"This is my bmi {bmi}")
if 18.5 <= bmi <= 25.5:
    print("You are underweight")
if 65 <= bmi <= 80:
    print("You are overweight")






