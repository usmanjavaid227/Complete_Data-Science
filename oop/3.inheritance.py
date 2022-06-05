class A:
    def displayA(self):
     print("A")
class B:
    def displayB(self):
      print("B")
class C(A,B):
    def displayC(self):
     print("C")

o=C()
o.displayA()
o.displayB()
o.displayC()


# multi_Level inheritance

# class A:
#     def displayA(self):
#      print("A")
# class B(A):
#     def displayB(self):
#       print("B")
# class C(B):
#     def displayC(self):
#      print("C")
