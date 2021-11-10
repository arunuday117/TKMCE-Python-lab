import operator
from collections import OrderedDict
months={'March':31,'February':28,'May':31,'January':31,'June':30,'October':31,'April':30,'July':31,'September':30,'November':30,'August':31,'December':31}
sort_al=(sorted(months.items(), key=operator.itemgetter(0)))
print("Months in alphabetical order ",sort_al)
x=input("Enter month name")
for i in months.keys():
    if i==x:
        print(months[i])
for i in months :
    if months [ i ] == 30 :
        print( i )
print("Months in ascending order ",sort_as)
