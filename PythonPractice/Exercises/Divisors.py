#ask user for number, then print a list of all divisors of that number

num = int(input("Please choose a number to divide: "))

listedRange = list(range(1,num+1))

divisorList = []

for i in listedRange:
    if num % i == 0:
        divisorList.append(i)
        
print(divisorList)