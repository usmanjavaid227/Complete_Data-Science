class DemoClass:
    a=20
    b=40
    
    def __init__(self):
        print("hello")

    # def sum(self,a,b):
    #     print(a+b)
    def sum(self):
        self.c = self.a+self.b
        print(self.c)
    
obj=DemoClass()
print(obj.a)
# obj.sum(50,60)
obj.sum()