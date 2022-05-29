print(" \n Welcome :\n This is a program to play with stack using list :\n\t Hope you will Enjoy\n\n\t\t (-_-) ")
l=[]
while True:
    a= int(input("""
            please select your choice:
            Enter No. :
            1  To add a element in list 
            2  To delete last elements
            3  To display the last element
            4  To display the list 
            5  To exit from the program
    """))
 
    if a==1:
        n=int(input("Enter The number you want to add :  "))
        l.append(n)
        print(l)
    elif a==2:
        if len(l)==0:
            print("Empty List stack : ")
        else:
            p=l.pop()
            print("You pop :- ",p)
    elif a==3:
         if len(l)==0:
            print("Empty List stack : ")
         else:
            print(" peek element : ",l[-1])
    elif a==4:
            print("Display List Stack : ",l)
    elif a==5:
        break
    else:
      print("Invalid input : ")
    
print("/t/t Thanks for you Time: ")

