class Student:
    "Information about the class"
    studentcount=0
    def getdata(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("No of student objects",Studnet.studentcount)
    def display(self):
        print("Roll no : ",self.roll)
        print("Name : ",self.name)
        print("Course : ",self.course)
s1=Student()
s2=Student()
s1.getdata(2008,"Reshma","MCA")
s2.getdata(2009,"Ananya","BTECH")
s1.display()
s2.display()
