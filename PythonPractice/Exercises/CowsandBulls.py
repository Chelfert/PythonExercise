# Randomly generate a 4-digit number. 
# Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 

import random

if __name__=="__main__":
    def cows_and_bulls():
        cows = 0
        bulls = 0
        count = 0
        gameChoice = str(random.randint(1000,9999))
        print (gameChoice) # show the game's number 
        while cows != 4:
            cows = 0
            bulls = 0
            userGuess = input("Please enter a 4 digit number: ") #ask user to guess a number
            while userGuess.isdigit() == False: # check if answer contains anything other than digits
                userGuess = input("Enter 4 numbers only : ")
            while len(userGuess) == 0: # catch empty inputs
                        userGuess = input("Empty Guess. Please enter a 4 digit number: ") 
            userGuess = int(userGuess) #convert to int to check if in range
            count += 1 # add to user count
            while userGuess not in range (1000,9999):
                userGuess = input("Number not 4 digits. Please enter a 4 digit number: ")#ask user to guess a number
                while len(userGuess) == 0: # if guess is empty, prompt again
                        userGuess = input("Empty Guess. Please enter a 4 digit number: ")
                userGuess = int(userGuess)
            userGuess = str(userGuess) #convert user's guess to str to iterate in range
            for i in range(4):
                if userGuess[i] == gameChoice[i]: # if user's choice is in the same place as the game's choice, add cow
                    cows += 1
                elif (userGuess[i] in gameChoice) and userGuess[i] != gameChoice[i]: #if user's guess is in the game's choice but not in the right place, add bull
                    bulls += 1
            print ("Cows: "+ str(cows),"Bulls: "+(str(bulls)))
            if cows == 4: # if all digits are in the right place, then end game and tell user their count!
                        print (f"Congratulations, you have won in {count} guesses!")
                        break  

cows_and_bulls()