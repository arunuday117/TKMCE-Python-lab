class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.area=length*breadth
    def disparea(self):
        print("Area of ",self.length," ",self.breadth," is ",self.area)
r1=Rectangle(10,20)
r2=Rectangle(20,30)
r1.disparea()
r2.disparea()
if r1.area<r2.area:
    print("Rectangle one has largest area")
