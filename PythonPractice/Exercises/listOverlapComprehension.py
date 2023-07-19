import random

#generate random list function
def randListGen(start,stop,range):
    x = 0
    randList = []    
    while x < range: 
        #gen random number
        randListNums = random.randint(start,stop)
        #add count to counter
        x = x + 1
        #append random number generated to randomlist
        randList.append(randListNums)
    return randList

#create random lists named 'A' and 'B' using function
A = (randListGen(1,100,8))
B = (randListGen(1,55,14))    

#create random lists using list comprehension
listComp1 = [random.randint(1,6) for i in range(1,random.randint(10,15))]
listComp2 = [random.randint(1,6) for i in range(1,random.randint(10,20))]
simList2 = set(listComp1).intersection(listComp2)

simList = set(random.randint(1,6) for i in range (1,random.randint(1,15))).intersection(random.randint(1,6) for i in range (1,random.randint(10,15)))

print ("These are the similar values %s " % simList)