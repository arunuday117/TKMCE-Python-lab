class Student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course

li=[]
n=int(input("Enter the no of students"))
for i in range(0,n):
    rollno=int(input("Enter the rollno : "))
    name=input("Enter the name : ")
    course=input("Enter the course : ")
    li.append(Student(rollno,name,course))
for ob in li:
    print(ob.roll,ob.name,ob.course)
    


