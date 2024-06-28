a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
if b==0:
    print("Division by zero is not possible ")
elif a%b==0:
    print(f"The remainder when {a} is divided by {b} is zero")
else:
    print(f"The remainder when {a} is diveded by {b} is ",a%b)    
