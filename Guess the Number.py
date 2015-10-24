# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
# will be a check for which option the player last selected
rangeOption = 0
remainingGuesses = 7

# helper function to start and restart the game
def new_game():
    # checks which button was last pressed and starts a new game in that range
    if rangeOption == 1:
        range1000()
    else:    
        range100()
# define event handlers for control panel
def range100():
    global remainingGuesses
    global secret_number
    global rangeOption
    secret_number = random.randrange(0,101)
    remainingGuesses = 7
    rangeOption = 0
    print "new game: Range is between between 0 - 100"

# define event handlers for control panel
def range1000():
    global remainingGuesses
    global secret_number
    global rangeOption 
    secret_number = random.randrange(0,1001)
    remainingGuesses = 10
    rangeOption = 1
    print "new game: Range is between 0 - 1000"

# define event handlers for control panel
def input_guess(guess):
    global remainingGuesses
    guessToInt = int(guess)   
    if remainingGuesses > 0 :        
            print "Your Guess Is: " + "[" + guess + "]"
            # when guess is entered, player losses a turn
            remainingGuesses -=  1 
            print "Number of guesses left: " + "[" + str(remainingGuesses)+ "]"
            if guessToInt > secret_number:
                print "Go Lower!"
                
            elif guessToInt < secret_number:
                print "Go Higher!"
                
            else:
                print "That's Correct!"
                print "... Let's play again ..." 
                new_game()      
    else:
            print "Sorry, you couldn't guess the number..."
            print "... Let's play again ..." 
            new_game()
        
    return guess        

# create frame
frame = simplegui.create_frame('Guess the Number',250, 250)

# add buttons
frame.add_button('0 - 100', range100, 100)
frame.add_button('0 - 1000', range1000, 100)

# register event handlers for control elements and start frame
frame.add_input('Input Guess Here: ', input_guess, 100)
frame.start()

# call new_game 
new_game()

