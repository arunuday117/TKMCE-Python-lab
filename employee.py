class Employee:
    def __init__(self,empid,empname,salary,dep):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        self.dep=dep
li=[]
n=int(input("Enter the no of employee"))
for i in range(0,n):
    empid=int(input("Enter the Employee ID : "))
    empname=input("Enter the Employee name : ")
    salary=int(input("Enter the Employee salary : "))
    dep=input("Enter the Employee Department : ")
    li.append(Employee(empid,empname,salary,dep))
for ob in li:
    if(ob.salary==15000):
        print(ob.empid,ob.empname,ob.salary,ob.dep)
