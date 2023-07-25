import random
#generates random passwords, either strong or weak
genPassword = []

def passwordGenerator(userLen):
    #for each number in user defined password length, choose randomly between random number, letter or special character and append to list
    for i in range(0,userLen):
        x = (random.randint(1,3))
        if x == 1:
            randInt = random.randint(0,9)
            genPassword.append((randInt))
        elif x == 2:
            alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            genPassword.append((random.choice(alphabet)))
        else:
            specialChars = ["!","@","$"]
            genPassword.append(random.choice(specialChars))
    return genPassword 

#ask user for strong or weak password
print ("Would you like a strong or weak password?")
userChoice = int(input("Please enter 1 for strong or 2 for weak: "))


#if strong, ask user how many characters they would like
if userChoice == 1:
    length = int(input("how many characters would you like in your password?: "))
    if length < 14:
        print ("That's not a very strong password, try entering more than 14...")
        length = input("how many characters would you like in your password?: ")
        length = int(length)
elif userChoice == 2:
    length = 10
    
#insert user length into password generator then convert it to a string
passwordGenerator(length)
stringPassword = ''.join([str(elem) for elem in genPassword])

#display password
print ("Your password is: "+stringPassword)