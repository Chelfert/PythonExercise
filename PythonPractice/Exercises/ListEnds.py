import random

def listEnds(userList):
    return [userList[0],userList[-1]] # take first value, and last value and return

randomList = [random.randint(1,100) for i in range(random.randint(4,14))] # create random list
eoList = listEnds(randomList) # pass random list into function

print (eoList) # print returned values
