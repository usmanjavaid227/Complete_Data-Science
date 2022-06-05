class std:
    __name="" # Private 
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name = name
        print(self.__name)

print("*"*30)
obj=std()
# obj.__name   => don't access as it is private
obj.setname('usman')
obj.getname()
print("*"*30)


