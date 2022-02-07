print("Existing File")
print("-------")

with open('pylab2.txt') as file:
    with open('pylab2w.txt','w') as filew:
        for line in file.readlines():
            print(line)
            if(len(line.split(" "))>5 and line[0].isupper()):
                filew.write(line)


print("\n\n")
print("New File")
print("-------")
with open('pylab2w.txt') as readfile:
    for line in readfile.readlines():
        print(line)
