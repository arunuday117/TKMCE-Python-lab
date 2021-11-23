def armstrong(num):
    sq=0
    val=num
    while(val>0):
        n=val%10
        sq+=n**3
        val=val//10
    return sq
num=int(input("Enter a number"))
a=armstrong(num)
if num==a:
    print(num," is a armstrong number")
else:
    print(num," is not a armstrong number")
