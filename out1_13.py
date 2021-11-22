s=input("Enter comma separated colors : ")
s=s.split(",")
l=[]
c=0
for i in s:
    l.append(i)
print("First color : ",l[0]," Last Color : ",l[-1])
