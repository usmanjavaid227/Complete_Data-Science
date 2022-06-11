import random
c_number=random.randint(1,100)
un=int(input("please enter a no. btw 0-101 :---"))
if c_number>un:
    print("computer Number  ",c_number)
    print("You guess is low")
elif c_number<un:
    print("computer Number :--- ",c_number)
    print("You guess is high")
else:
    print("computer Number :--- ",c_number)
    print("You guess is good")