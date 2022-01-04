class Student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("Roll No : ",self.roll)
        print("Name : ",self.name)
        print("Course : ",self.course)
class Test(Student):
    def __init__(self,roll,name,course,mark):
        Student.__init__(self,roll,name,course)
        self.mark=mark
    def displaymark(self):
        self.display()
        print("Marks : ",self.mark)
s1=Test(100,'Amal','MCA',98)
s1.displaymark()
