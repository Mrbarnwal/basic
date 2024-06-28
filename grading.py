f1= int(input("Enter full marks: "))
m1= int(input("Enter the marks of coresponding subject: "))
f2= int(input("Enter full marks: "))
m2= int(input("Enter the marks of coresponding subject: "))
f3= int(input("Enter full marks: "))
m3= int(input("Enter the marks of coresponding subject: "))
t_marks= f1 + f2 + f3 
c_marks= m1 + m2 + m3
if f1==0 or f2==0 or f3==0:
    print("Lichad panti mat kriye")
elif ((100*(c_marks)/t_marks)>90):
    print("Your grade is A")
elif (90>(100*(c_marks)/t_marks)>80):
    print("Your grade is B ")
elif (80>(100*(c_marks)/t_marks)>70):
    print("Your grade is C ")
elif (70>(100*(c_marks)/t_marks)>60):
    print("Your grade is ")
elif (60>(100*(c_marks)/t_marks)>50):
    print("Your grade is ")
else:
    print("Better luck next time")