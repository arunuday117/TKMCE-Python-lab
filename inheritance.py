class Student:
    def getdata(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("Roll No : ",self.roll)
        print("Name : ",self.name)
        print("Course : ",self.course)
class Test(Student):
    def getmarks(self,mark):
        self.mark=mark
    def displaymark(self):
        self.display()
        print("Marks : ",self.mark)
s1=Test()
s1.getdata(101,'Amal','MCA')
s1.getmarks(89)
s1.displaymark()
