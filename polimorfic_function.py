#Polymorphism via Inheritance
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side

# Polymorphic function using inheritance
def calculate_area(shape):
    print(f"The area is: {shape.area()}")

calculate_area(Circle(5)) # The area is: 78.5
calculate_area(Square(4)) # The area is: 16



#======================
#Parametric Polymorphism (Abstract Base Classes)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPal(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via PayPal")

def execute_payment(payment_method, amount):
    payment_method.process(amount)

'''How it Functions
When you call execute_payment(payment_method, amount), the function doesn't know (or care) if it is dealing with a CreditCard object, a PayPal object, or a Crypto object. It only cares that the object has a .process() method.

1. The Interface (The "Contract")
The payment_method expects an object that implements the process method. In the previous example, we used an Abstract Base Class (ABC) to define this contract.

Python
def execute_payment(payment_method, amount):
    # This is the polymorphic call
    # payment_method could be a CreditCard instance or a PayPal instance
    payment_method.process(amount)
'''
