from getpass import getpass
p1name = input("Player 1, what is your name: ")
p2name = input("Player 2, what is your name: ")

#define rules of game
def Game(p1,p2,u1,u2):
        if p1 == p2:
                return("it's a tie!")
        elif p1 == "rock":
                if p2 == "scissors":
                    return (u1+" wins!")
                else:
                    return(u2+" wins!")
        elif p1 == "scissors":
                if p2 == "paper":
                        return(u1+" wins!")
                else:
                        return(u2+" wins!")
        elif p1 == "paper":
                if p2 == "rock":
                        return(u1+" wins!")
                else:
                        return(u2+" wins!")
        else:
                return("Invalid input! Please enter rock, paper or scissors.")


#while play is true, continue playing in loop
play = True

while play == True:
    
    #prompt players for choices
    print(p1name+", please choose rock, paper or scissors: ")
    P1Choice = getpass()

    print(p2name+", please choose rock, paper or scissors: ")
    P2Choice = getpass()

    
    #show outcome of game
    print(Game(P1Choice,P2Choice,p1name,p2name))
    #end game
    gameOver = True
    
    #end game and ask user if they want to play again
    while gameOver == True:
        playChoice = str(input("Would you like to play again? y or Y for yes, n or N for no: "))
        if playChoice == "y" or playChoice =="Y":
            play = True
            gameOver = False
        elif playChoice == "n" or playChoice == "N":
            play = False
            print("Thanks for playing!")
            exit()
            