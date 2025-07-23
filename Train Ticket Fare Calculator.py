name=input("enter your name")
age=float(input("enter your age"))
distance=float(input("distance in km's"))
class_=int(input("choose your class through 1,2,3 \n1.General\n2.sleeper\n3.AC\nr"))
general=float(1)
sleeper=float(2)
ac=float(3)
print("passenger:",name)
print("age:",age)
if class_==1:
    print("base fare:",distance*general)
    if age<5:
        print("discount:100%")
    elif age>=5 and age<=12:
        print("discount:50%")
    elif age>=60:
        print("discount:30%")
    else:
        print("no discount")
elif class_==2:
    print("base fare:",distance*sleeper)
    if age<5:
        print("discount:100%")
    elif age>=5 and age<=12:
        print("discount:50%")
    elif age>=60:
        print("discount:30%")
    else:
        print("no discount")
elif class_==3:
    print("base fare:",distance*ac)
    if age<5:
        print("discount:100%")
    elif age>=5 and age<=12:
        print("discount:50%")
    elif age>=60:
        print("discount:30%")
    else:
        print("no discount")
