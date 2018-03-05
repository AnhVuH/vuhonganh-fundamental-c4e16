height = int(input("Height(cm): "))*0.01
weight = int(input("Weight(kg): "))
bmi = weight/(height* height)
if bmi < 16:
    print ("Severely  underweight")
elif bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
