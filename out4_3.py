class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.area=length*breadth
    def __lt__(self,m):
        return self.area<m.area
r1=Rectangle(50,20)
r2=Rectangle(20,30)
if r1<r2:
    print("Rectangle one has largest area")
else:
    print("Rectangle two has largest area")
