t_bill=float(input("enter total bill"))
t_people=float(input("enter total number of people"))
tip_percentage=float(input("enter tip percentage"))
tip=t_bill/tip_percentage
t_bill_with_tip=t_bill+tip
each_pay=t_bill_with_tip/t_people
print("total with tip :",t_bill_with_tip)
print("each person should pay",each_pay)
if    each_pay>100:
    print("wow thats an expensive dinner")

if    each_pay>=50 and each_pay<=100:
 print("fancy night out")

if    each_pay<50:
    print("its affordable")