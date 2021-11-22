print("Enter three value:")
a,b,c=input(),input(),input()
if((a>b) and (a>c)):
    print(a, "is greater")
elif ((b>a) and (b>c)):
    print(b, "is greater")
else:
    print(c, "is greater")
print(max(a,b,c))
