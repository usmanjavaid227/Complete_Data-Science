print(" \n Welcome :\n This is a program to play with Queue using list :\n\t Hope you will Enjoy\n\n\t\t (-_-) ")
l=[]
while True:
    a= int(input("""
            please select your choice:
            Enter No. :
            1  To add a element in list 
            2  To delete last elements
            3  To display the first element
            4  To display the last element
            5  To display the list 
            6  To exit from the program
    """))
 
    if a==1:
        n=int(input("Enter The number you want to add(Enqueue) :  "))
        l.append(n)
        print(l)
    elif a==2:
        if len(l)==0:
            print("Empty List Queue : ")
        else:
            del l[0]
    elif a==3:
         if len(l)==0:
            print("Empty List Queue : ")
         else:
            print(" first element : ",l[0])
    elif a==4:
         if len(l)==0:
            print("Empty List Queue : ")
         else:
            print(" last element : ",l[-1])
    elif a==5:
            print("Display List Queue : ",l)
    elif a==6:
        break
    else:
        print("Invalid input : ",)
    
print(" Thanks for you Time: ")

