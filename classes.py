class rect:
    l=0
    w=0
    def __init__(self,x,y):
        self.l=x
        self.w=y

    def area(self):
        print("Area is ", self.l*self.w)

    def perimeter(self):
        print("Perimeter is ",2*(self.l+self.w))

r1=rect(5,6)
# r2=rect(7,8)
# r3=rect(9,5)
# r1.area()
# r2.area()
# r3.area()
r1.perimeter()
# print(r3.w)

# Single Level Class Inheritance
class square(rect):
    pass
s=square(4,4)
s.area()

# Other Example of single level inheritance
class square(rect):
    def area (self):
        print("hahahahahaa")
    def here (self):
        print("here")
        self.area()
        super().area()
        print(super().w)
s=square(4,4)
s.here()

# Multi-Level class Inheritance
class temp(square):
    pass

# Multiple inheritance
class demo (rect,square):
    pass

