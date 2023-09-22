#BMI Calculator
#BMI Equation: BMI = (Weight(kg)/height^2(m)

while True:
    print ("Find your BMI score\n")
    height = float(input("Enter your height in metres: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = weight/height**2
    print (bmi)
    restart = input("Restart BMI Calculator: (Y/N)\n").lower()
    if restart != "y":
        print("Exiting BMI Calculator.")
        break
    print("Restarting BMI Calculator...\n")
