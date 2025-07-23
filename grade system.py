name=input("enter your name")
sub1=int(input("enter subject1 marks out of 100 :"))
sub2=int(input("enter subject2 marks out of 100 :"))
sub3=int(input("enter subject3 marks out of 100 :"))
t_marks=sub1+sub2+sub3
t_marksreal=float(t_marks)
a_marks=t_marksreal/3
a_marksreal=float(a_marks)
print("Student:",name)
print("Total Marks:",t_marksreal)
print("Average:",a_marksreal)
if a_marksreal>=90 and a_marksreal<=100:
    print("GRADE:A+")
    print("Excellent work!")
elif a_marksreal>=80 and a_marksreal<=89:
    print("GRADE:A")
    print("Excellent work!")
elif a_marksreal>=70 and a_marksreal<=79:
    print("GRADE:B")
    print("Good job, but there's room to improve.")
elif a_marksreal>=60 and a_marksreal<=69:
    print("GRADE:C")
    print("Good job, but there's room to improve.")
elif a_marksreal>=50 and a_marksreal<=59:
    print("GRADE:D")
    print("You passed, but study harder.")
else:
    print("GRADE:F")
    print("You failed. Better luck next time.")
