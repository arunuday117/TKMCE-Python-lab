num=int(input("Enter a number"))
a=0
b=1
sum=0
count=1
print("Fibonacci series\n")
while count<=num:
    print(sum,"\n")
    a=b
    b=sum
    sum=a+b
    count+=1
