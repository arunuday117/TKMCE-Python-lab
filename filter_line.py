s=input("Enter a line of text")
l=list(s.split(" "))
l1=list(filter(lambda x:x.isupper(),l))
print(l1)
