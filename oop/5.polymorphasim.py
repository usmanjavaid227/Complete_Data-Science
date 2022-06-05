# Overloading this method
# class A:
#     def display(self,name=""):
#         print("usman javaid"+name)

# o=A()
# o.display()
# o.display(" Mughal")

# override

class A():
    def display(self):
        print("A")
class B(A):
    def display(self):
        super().display()
        print("B")

o=B()
o.display()
