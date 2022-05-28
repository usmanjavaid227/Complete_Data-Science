
i="Y"
while i=="Y" or i=='y':
    num1=int(input("Enter 1st number : "))
    num2=int(input("Enter 2nd number : "))
    op=input("""
    + for addition
    - for subtraction
    * for multiplication
    / for division
    please Enter the operator """)

    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="*":
        print(num1*num2)
    elif op=="/":
        print(num1/num2)
    else:
        print("You Enter invalid Operator!")
    i=input("Enter Y to proceed again :")
print("Thank")
        
