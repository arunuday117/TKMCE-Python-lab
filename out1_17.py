import operator
d={3:5,1:3,4:2,5:1,2:4}
sort_as=(sorted(d.items(), key=operator.itemgetter(0)))
sort_dec=(sorted(d.items(), key=operator.itemgetter(0), reverse=True))
print("Dictionary sorted ascending order ",sort_as)
print("Dictionary sorted descending order ",sort_dec)
