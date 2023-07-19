#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

 #   If the number is a multiple of 4, print out a different message.
  #  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.



num = int(input("Please pick a number: "))
check = int(input("Please pick a number to divide the first number by: "))


#see if check divides into num evenly, if so print, if not print else
if num % 4 == 0:
    print("This number is divisible by 4")

elif num % check == 0:
    print("The number is even, very nice")
else:
    print("The number is odd, dang")
