import random

#set user guess count
guessCount = 0

playGame = True
playAgain = 0

#gen random number
gameNum = random.randint(1,9)

print("Welcome to the guessing game, whenever you're tired of playing type %s" % str("'exit'"))

while playGame:
    #ask user to guess number
    userGuess = input("Please guess a number between 1 and 9: ")
    #if too low or high, add guesscount and prompt again
    if userGuess == "exit":
        print("Thanks for playing, cya")
        break
        
    #convert guess to int
    userGuess = int(userGuess)
    guessCount += 1
    
    if userGuess < gameNum:
        userGuess = print("Your guess was too low, guess again: ")
    elif userGuess > gameNum:
        userGuess = print("Your guess was too high, guess again: ")
    elif userGuess == gameNum:
        print("Congratulations, You guessed the correct number in %s guesses!" % guessCount)
        #reset guess count and user guess
        playGame = not playGame

            

#tell them whether they have guessed too high or too low
#add count to guesscount
#when user guesses correctly, end game, tell them guesscount and ask if they want to play again