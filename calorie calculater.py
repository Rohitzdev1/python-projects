name=input("enter your name:")
age=input("enter your age:")
steps=float(input("enter today'steps :"))
calories_burned=steps*0.04
print("hello",name,"at",age,"you walked",steps,"today and burned ",calories_burned)
if    calories_burned>300:
    print("Great job staying active! 💪")
if    calories_burned<300:
    print("try to move a bit more ")