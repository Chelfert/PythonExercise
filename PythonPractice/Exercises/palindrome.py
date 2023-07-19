#ask user for string
#save string in variable (strings are lists)
#create string off of variable, create string off of reversing the variable
#if string1 == string2, then print this is a palindrome, else print this is not a palindrome

#user's choice
userWord = input("Please enter a word: ")
userWord = userWord.lower()

#create empty lists
newWord = []
reverseWord = []

#put userword into new list
for i in (userWord):
    newWord.append(i)

#put reversed word into new list
for i in reversed(userWord):
    reverseWord.append(i)
    

if reverseWord == newWord:
    print("This is a palindrome")
else:
    print("This is not a palindrome")