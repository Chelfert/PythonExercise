import sys
def isPrime(number):
    if number > 0:
        for i in range (2,number - 1): # 1 through number minus 1
            if number % i != 0: # if number can't be divided by i cleanly, then continue to next
                continue
            elif number % i == 0: # if number can be divided, then it isn't prime
                sys.exit("This number is not prime.")
        sys.exit("The Number is prime.") # when i runs out of range, then exit and tell user number was prime
    elif number == 0:
        sys.exit("Number is not prime") # if number is 0, then it can't be prime
    else:
        sys.exit("Number is not prime.") # if number is negative, then it can't be prime


userNum = input("Please enter a number to see if it is prime: ") # user enters number to see if prime
userNum = int(userNum) # convert input to int

isPrime(userNum) # call function and pass user number

        