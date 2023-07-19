#take predetermined list and grab the even numbers and put them in a new list
#grab modulus of numbers, if % 2 == 0 then move it to array, else don't
givenList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenList = []

for i in givenList:
    if i % 2 == 0:
            evenList.append(i)
    else:
        continue
    
print(evenList)