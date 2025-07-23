name=input("enter your name")
height=float(input("enter your height in meters"))
weight=float(input("enter your weight in kgs"))
bmi=weight/(height*height)
if   bmi<18.5:
    print("BMI :","underweight")
if    24.9>bmi>=18:
        print("BMI:","NORMAL WEIGHT")
if   25<bmi<29.9:
            print("BMI:","over weight")
if    bmi>=30:
                print("BMI:","OBESE")