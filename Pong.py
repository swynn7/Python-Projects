# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

# template included variables
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# added variables
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
paddle1_pos = [0, 0]
paddle2_pos = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    if direction == RIGHT:
        
        ball_vel[0] = random.randrange(120, 241)/60
        ball_vel[1] = - (random.randrange(60, 181)/60)
                
    elif direction == LEFT:
       
        ball_vel[0] = - (random.randrange(120, 241)/60)  
        ball_vel[1] = -(random.randrange(60, 181)/60)

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0 
    score2 = 0
    ball_pos [0] = WIDTH/2
    ball_pos [1] = HEIGHT/2
    spawn_ball(random.choice([LEFT, RIGHT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    
    # midlines
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    # left gutter
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    # right gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
      
    # update ball   
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # bottom collision
    if ball_pos[1] >= HEIGHT - BALL_RADIUS * 2:
        ball_vel[1] = - ball_vel[1]
        
        # test
        # print "bottom: " + str(print ball_vel[1])

    # top collision     
    elif ball_pos[1] <= HEIGHT - HEIGHT + BALL_RADIUS:
        ball_vel[1] = abs(ball_vel[1])
        
        # test
        # print "top: " + str(print ball_vel[1])
        
    # left collision
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        
        # test
        # print "this is the ball position: " + str(ball_pos[1])
        
        # determine whether paddle and ball collide
        if ball_pos[1] >= (paddle1_pos[1]) and ball_pos[1] <= (paddle1_pos[1] + PAD_HEIGHT):
            # reflects ball horizontally right
            ball_vel[0] = abs(ball_vel[0])
            # increase velocity by 10%
            ball_vel[0] += ball_vel[0]/10
            ball_vel[1] += ball_vel[1]/10
            
        else:
            ball_pos [0] = WIDTH/2
            ball_pos [1] = HEIGHT/2
            spawn_ball(RIGHT)
            score2 += 1
        
    # right collision
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS: 
        
        # test
        # print "this is the ball position: " + str(ball_pos[1])
        
        # determine whether paddle and ball collide
        # orient ball position values for right paddle, run above test while printing y values for paddle 2 in keydown event
        if (-(ball_pos[1]) + HEIGHT) >= -(paddle2_pos[1]) and (-(ball_pos[1]) + HEIGHT) <= -(paddle2_pos[1]) + PAD_HEIGHT:
        # reflects ball horizontally right
            ball_vel[0] = - ball_vel[0]
        # increase velocity by 10%
            ball_vel[0] += ball_vel[0]/10
            ball_vel[1] += ball_vel[1]/10    
            
        else:
            ball_pos [0] = WIDTH/2
            ball_pos [1] = HEIGHT/2
            spawn_ball(LEFT)
            score1 += 1 
        
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    
    # prevents paddles from leaving canvas
    
    # bottom check
    if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
    # top check    
    elif paddle1_pos[1] <= HEIGHT - HEIGHT:
        paddle1_pos[1] = HEIGHT - HEIGHT
    # bottom check    
    if paddle2_pos[1] >= HEIGHT - HEIGHT:
        paddle2_pos[1] = HEIGHT - HEIGHT
    # top check    
    elif paddle2_pos[1] <= PAD_HEIGHT - HEIGHT:
        paddle2_pos[1] = PAD_HEIGHT - HEIGHT 

    # draw paddles
    
    # left paddle
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos[1]], [HALF_PAD_WIDTH, PAD_HEIGHT + paddle1_pos[1]], PAD_WIDTH, "Red")    
    # right paddle
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, HEIGHT + paddle2_pos[1]], [WIDTH - HALF_PAD_WIDTH, HEIGHT - PAD_HEIGHT + paddle2_pos[1]], PAD_WIDTH, "Blue")          
    
    # draw scores
    
    # left score
    canvas.draw_text(str(score1), [WIDTH/2 - PAD_WIDTH * 10 , HEIGHT/5], 50, "Green")
    # right score
    canvas.draw_text(str(score2), [WIDTH/2 + PAD_WIDTH * 7, HEIGHT/5], 50, "Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
    
    vel = 5

    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -(vel)
        #print paddle1_pos[1]

    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = vel
        # print paddle1_pos[1]

    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -(vel)
        #print paddle2_pos[1]
        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = vel
        #print paddle2_pos[1]
                                   
def keyup(key):
    global paddle1_vel, paddle2_vel
    # stop paddles from moving if no keydown event
    paddle1_vel[1] = 0
    paddle2_vel[1] = 0

# create frame

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 75)

# start frame

new_game()
frame.start()

print "Think I made the right/blue paddle more complicated than it needed to be \
if anybody has the time would you mind looking at the coding associated with that paddle \
and provide feedback. Thanks! "