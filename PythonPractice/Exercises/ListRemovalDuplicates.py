#take a list that contains no duplicates of an original list

#original list containing duplicates
dupes = [1,2,3,3,3,4,4,5,8,8,9,9,9]

#function that creates set out of list
def removeDuplicates(dupes):
    noDupe = set()
    for i in dupes:
        noDupe.add(i)
    print (noDupe)

#call function
removeDuplicates(dupes)
