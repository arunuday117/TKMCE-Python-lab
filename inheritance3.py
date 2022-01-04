class Student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("Roll No : ",self.roll)
        print("Name : ",self.name)
        print("Course : ",self.course)
class Mark:
    def __init__(self,mark):
        self.mark=mark
    def displaymark(self):
        print("Marks : ",self.mark)
class Details(Student,Mark):
    def __init__(self,roll,name,course,mark,hostelflag):
        Student.__init__(self,roll,name,course)
        Mark.__init__(self,mark)
        self.hostelflag=hostelflag
    def displayflag(self):
        self.display()
        print("Marks : ",self.mark)
        print("Hostel Flag : ",self.hostelflag)
s1=Details(101,'Athul','MCA',97,False)
s1.displayflag()
