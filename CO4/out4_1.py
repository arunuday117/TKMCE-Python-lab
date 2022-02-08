class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=self.length*self.breadth
        return self.area
    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        return self.perimeter

l1=int(input("Enter the length of the first rectangle : "))
b1=int(input("Enter the breadth of the first rectangle : "))
l2=int(input("Enter the length of the second rectangle : "))
b2=int(input("Enter the breadth of the second rectangle : "))
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
a1=r1.area()
a2=r2.area()
print("\nArea of the first rectangle : ",a1)
print("Perimeter of the first rectangle : ",r1.perimeter())
print("\nArea of the second rectangle : ",a2)
print("Perimeter of the second rectangle : ",r2.perimeter())

if a1>a2:
    print("\nFirst reactangle has the largest area : ",a1)
else:
    print("\nSecond reactangle has the largest area : ",a2)

    
