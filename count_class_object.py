# class obj:
#     count=0
#     def __init__(self, id, name):
#             self.id=id
#             self.name =name
#             obj.count+=1
#             print(self.id, self.name)
# o1=obj(1,'a')
# o2 = obj(2,'b')
# o3 = obj(3,'c')
# print("call object",obj.count)

'''
swapcase() :- This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.
str3 = str.swapcase();
print (" The swap case converted string is : " + str3) #The swap case converted string is : gEEKSfORgEEKS IS FoR gEEkS
'''


#======================
# delete class
class A:
    def f(self, x):
        print("jhfgwjrh", x)

class B(A):
    def fun(self):
        print("jjhgfsdjhh")
del A
o = B()
print(o.f(4)) # call f (function) with class B object then it will work fine because B already inherit A class property,
#while class A already call with del function before B object creation.
o1 = A() # here through error because class A is deleted



# delete class method
class MyClass:
    def my_function(self):
        print("Hello")

# Delete the function from the class
del MyClass.my_function
o = MyClass()
print(o.my_function()) # through Attribute error because myfuntion already deleted
