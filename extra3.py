l=[1,2,3,4,5]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Odd ",odd)
print("Even ",even)
