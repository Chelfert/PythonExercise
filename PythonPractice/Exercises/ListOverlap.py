#take common occurences from two lists and combine into one
a = [1,3,4,5,7,8,34,66,55,87,26,75]
b = [1,2,3,4,5,6,7,8,9,10,15,55,87]

#print (4 in a)
newList = list(set([x for x in a if x in b]))

print (newList)

        