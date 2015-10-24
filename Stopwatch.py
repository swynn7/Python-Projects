# template for "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
totalStops = 0
correctStops = 0
width = 450
height = 250
interval = 100
buttonSize = 75
stopWatchRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    # get millisecond
    d = t % 10 
    
    # get seconds
    c = t % 100 // 10
    b = t // 100 % 6    
    
    # get minutes
    a = t // 600
    
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

#print format(0)
#print format(11)
#print format(321)
#print format(613)

# define event handlers for buttons; "Start", "Stop", "Reset"
def startTimer():
    global stopWatchRunning
    stopWatchRunning = True
    timer.start()

def stopTimer():
    global totalStops, correctStops, stopWatchRunning
    
    # print counter    
    if stopWatchRunning == True:
        if counter % 10 == 0:
            correctStops += 1
            totalStops += 1
            
        else:
            totalStops += 1
            
    stopWatchRunning = False
    timer.stop()
         
def resetTimer():    
    global counter, totalStops, correctStops, stopWatchRunning
    counter = 0
    totalStops = 0
    correctStops = 0
    stopWatchRunning = False
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1
    # print counter

# define draw handler
def draw_handler(canvas):
    global counter, totalStops, correctStops
    canvas.draw_text(format(counter), (width/3, height/2), 60, "Purple")
    canvas.draw_text(str(correctStops) + "/" + str(totalStops), (width-50,height-225), 20, "Blue")

# create frame
frame = simplegui.create_frame("StopWatch", width, height)
frame.set_canvas_background("Gray")

# register event handlers
start = frame.add_button("Start", startTimer, buttonSize)
stop = frame.add_button("Stop", stopTimer, buttonSize)
reset = frame.add_button("Reset", resetTimer, buttonSize)
draw = frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()

