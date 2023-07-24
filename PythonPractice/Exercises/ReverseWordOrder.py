#ask user for string, then print the string in reverse order

def reversePhrase(x):
    #create list of words separated by whitespace
    result = x.split(" ")
    #create list in reverse order
    reverseResult = result[::-1]
    #print every item in list
    for i in reverseResult:
        print (i)
        
#ask user for input        
userIn = input ("Please enter a string of words you want to reverse: ")

reversePhrase(userIn)

