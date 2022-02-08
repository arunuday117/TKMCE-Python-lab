from graphics import rectangle
from graphics import circle
from graphics.threed_graphics import sphere
from graphics.threed_graphics import cuboid

l=int(input("Enter the length of the rectangle : "))
b=int(input("Enter the breadth of the rectangle : "))
print("Area of the rectangle : ",rectangle.area(l,b))
print("Perimeter of the rectangle : ",rectangle.perimeter(20,30))
r=int(input("Enter the radius of the circle : "))
print("Area of the circle : ",circle.area(r))
print("Perimeter of the circle : ",circle.perimeter(r))
l=int(input("Enter the length of the cuboid : "))
b=int(input("Enter the breadth of the cuboid : "))
h=int(input("Enter the height of the cuboid : "))
print("Surface Area of the cuboid : ",cuboid.area(l,b,h))
print("Perimeter of the cuboid : ",cuboid.perimeter(l,b,h))
r=int(input("Enter the radius of the sphere : "))
print("Surface area of the sphere : ",sphere.area(r))
print("Perimeter of the sphere : ",sphere.perimeter(r))
