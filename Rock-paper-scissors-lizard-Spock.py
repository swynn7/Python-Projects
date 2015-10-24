# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
def name_to_number(name):
    
    # convert name to number using if/elif/else
    if   name == "rock"   :
         name = 0
        
    elif name == "Spock"  :
         name = 1
        
    elif name == "paper"  :
         name = 2
        
    elif name == "lizard" :
         name = 3
        
    else                  :
         name = 4
    
    # don't forget to return the result!
    return name	

def number_to_name(number):
    
    # convert number to a name using if/elif/else    
    if   number == 0      :
         number = "rock"
        
    elif number == 1      :
         number = "Spock"
        
    elif number == 2      :
         number = "paper"
        
    elif number == 3      :
         number = "lizard"
        
    else                  :
         number = "scissors"
            
    # don't forget to return the result!
    return number

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print " "
    
    # print out the message for the player's choice
    print "Player chooses " + "[ " + player_choice + " ]"
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + "[ " + comp_choice + " ]"	
    
    # compute difference of comp_number and player_number modulo five
    comp_player_result = (comp_number - player_number) % 5
        
    # use if/elif/else to determine winner, print winner message
    if comp_player_result == 0  :
        print "It's a tie!"
        
    elif comp_player_result <= 2:  
        print "Computer wins!"        
        
    else                        :     
        print "Player wins!"
        
    return player_choice
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


