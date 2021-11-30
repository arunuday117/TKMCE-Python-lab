import functools
l=[1,2,3,4,5]
print(l)
n=functools.reduce(lambda x,y:x+y,l)
print(n)
