fr=open("test.txt","r")
fw=open("newtest.txt","w")
i=1
for line in fr.readlines():
    if i%2!=0:
        fw.write(line)
    i=i+1
fr.close()
fw.close()
fr=open("test.txt","r")
print("initial file")
for line in fr.readlines():
    print(line)
f=open("newtest.txt","r")
print("\n\n\nNew file")
for line in f.readlines():
    print(line)
    
fr.close()
fw.close()
