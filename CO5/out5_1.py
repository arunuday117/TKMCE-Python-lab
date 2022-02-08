fr=open("test.txt","r")
l=[]
for line in fr.readlines():
    l.append(line)
print(l)
fr.close()
