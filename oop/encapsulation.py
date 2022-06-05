import sys
class bank:
    def __init__(self): #constructor
        print("Enter your account details :") 
        self.__account_no= int(input("Enter account number : "))
        self.__balance= int(input("Enter  balance : "))
    def diposit(self):
        self.amount= int(input("Enter amount that you want to deposit :"))
        self.__balance = self.__balance+self.amount
    def withdraw(self):
        self.withdraw= int(input("Enter withdraw amount that you want to withdraw :"))
        self.__balance=self.__balance-self.withdraw
    def display(self):
        print("Your balance is :", self.__balance)     



b1=bank()
while True:
    print("*"*30) 
    
    # b1.input()
    print("Press 1 to deposit amount :") 
    print("Press 2 to withdraw amount :")
    print("Press 3 to display balance :") 
    print("Press 4 to exit :") 
    print("*"*30)
    number= int(input("Enter your choice :"))
 
    if number ==1:
        b1.diposit()
    elif number ==2:
        b1.withdraw()
    elif number ==3:
        b1.display()
    elif number ==4:
        sys.exit()







