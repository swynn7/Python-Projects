# implementation of card game - Memory

import simplegui
import random

frame_width = 800
frame_height = 100
card_deck_one = range(0,8)
card_deck_two = range(0,8)
complete_card_deck = card_deck_one + card_deck_two
deck_pos_x = 0
deck_pos_y = frame_height
card_width = 50
card_height = 100
game_state = 0
counter = 0
previous_two_cards_value = range(2)
exposed = [False, False, False, False,
           False, False, False, False,
           False, False, False, False,
           False, False, False, False]

# helper function to initialize globals
def new_game():
    global exposed, game_state, counter
    random.shuffle(complete_card_deck)
    counter = 0
    label.set_text("Turns = " + str(counter))
    game_state = 0
    for e in range(len(exposed)):
        exposed [e] = False
            
# define event handlers
def mouseclick(pos):
    global exposed, game_state, previous_two_cards_value, counter
    
    # add game state logic here
    card_select = pos[0]//50
    if exposed[card_select]:
        return 
    exposed[card_select] = True
        
    if game_state == 0:
        previous_two_cards_value [0] = card_select
        game_state = 1
        
    elif game_state == 1:
        previous_two_cards_value [1] = card_select
        game_state = 2
        
    else:       
        if complete_card_deck[previous_two_cards_value [0]] != complete_card_deck[previous_two_cards_value [1]]:
            exposed[previous_two_cards_value[0]] = False
            exposed[previous_two_cards_value[1]] = False
                       
        previous_two_cards_value [0] = card_select
        counter += 1
        label.set_text("Turns = " + str(counter))
        game_state = 1
        
    #print previous_two_cards_value
    #print complete_card_deck[previous_two_cards_value[0]]
    #print complete_card_deck[previous_two_cards_value[1]]
                                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    global exposed, game_state 
    font_size = 75
    
    for i in range(len(complete_card_deck)) and range(len(exposed)):
            
            if exposed[i] == True:
                    
                frame.set_canvas_background("Black")                
                canvas.draw_text(str(complete_card_deck[i]),(i * card_width, deck_pos_y - 25), font_size, "Gray")                    
                  
            elif exposed [i] == False:
                
                canvas.draw_polygon([(i* card_width + 25, 0),(i* card_width + 25, deck_pos_y ),((i* card_width + card_width - 25), deck_pos_y ),((i* card_width + card_width - 25), 0)], card_width, "Purple")                                
                canvas.draw_line((i * card_width, deck_pos_y - deck_pos_y), (i * card_width, deck_pos_y), 1, "Gray")                 

            #print exposed

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frame_width, frame_height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric