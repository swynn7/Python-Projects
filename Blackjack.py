# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
dealer_value = ""
player_value = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos): 
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        s = "Hand contains: "
        for i in range(len(self.hand)):
            s += str(self.hand[i]) + " "
        return s
    
    def add_card(self, card):
        self.card = card
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        hand_value = []
        self.value = 0
        for i in range(len(self.hand)):
            
            #test
            #print type (self.hand[0])
            
            value = VALUES.get(str(self.hand[i].get_rank()))
            
            # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
            if value == 1:
                value = 1
                if self.value < 11:
                    value += 10
                    self.value = value
                else:
                    value = 1
                    self.value = value
                    
            hand_value.append(value)            
            self.value = sum(hand_value)
        
        return self.value
        
    def draw(self, canvas, pos):
        self.pos = pos
        self.canvas = canvas
        x = pos[0]
        y = pos[1]
        # draw a hand on the canvas, use the draw method for cards        
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, (x * i + CARD_SIZE[0], y))
            
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i], RANKS[j]))               

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        self.deal = self.deck.pop()
                
        return self.deal
    
    def __str__(self):
        # return a string representing the deck
        s = "Deck contains: "
        for i in range(len(self.deck)):
            s += str(self.deck[i]) + " "            
        return s
    
#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, score, dealer_value, player_value, deck    
    
    if in_play == True:
        score -= 1  
        outcome = "Penalty for new deal, -1"
        in_play = False
        
    else:
        dealer_value = ""
        player_value = ""
        dealer = Hand()
        player = Hand()
        deck = Deck()
        deck.shuffle()
    
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    
        outcome = "Hit or stand?"
        in_play = True
        
    #test
    #print "- dealer -"
    #print dealer
    #print dealer.get_value()
    #print "- player -"
    #print player
    #print player.get_value()
        
def hit(): 
    global in_play, player, outcome, score    
    
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
        outcome = "Hit again?"

        #test
        #print "- player -"
        #print player
        #print player.get_value()
        
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            in_play = False
            score -= 1        
            outcome = "You Busted! :("
            print "You Busted! :("

            #test
            #print player.get_value()
        
def stand():   
    global in_play, dealer, outcome, score, dealer_value
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            score += 1
            outcome = "Dealer Busted, You Win!"
            print "Dealer Busted, You Win!"
            
            #print "- dealer -"
            #print dealer
            #print dealer.get_value()
            
        elif dealer.get_value() < player.get_value():  
            score += 1 
            outcome = "You Win! Deal again?"
            print "You Win! Deal again?"
            
            #test
            #print "- dealer -"
            #print dealer
            #print dealer.get_value()
                    
        elif dealer.get_value() >= player.get_value():  
            score -= 1
            outcome = "The dealer wins!"    
            print "The dealer wins!"
            
            #test
            #print "- dealer -"
            #print dealer
            #print dealer.get_value()
    
        in_play = False      
                 
# draw handler    
def draw(canvas):
    global deck, dealer, player, in_play
    player_value = player.get_value()  
    dealer_value = dealer.get_value()
    color = ["Blue", "Purple", "Gray", "White"]
    
    # test 
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])
    
    dealer.draw(canvas, [50, 175])      
    player.draw(canvas, [50, 325])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 175 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        dealer_value = ""
    
    canvas.draw_text("dealer:" + str(dealer_value), (50, 165), 30, "White", "monospace")
    canvas.draw_text("player:" + str(player_value), (50, 315), 30, "White", "monospace")
    canvas.draw_text("Blackjack", (50, 75), 75, "White", "monospace")
    canvas.draw_text("Score " + str(score), (485, 585), 15, "White", "monospace")
    canvas.draw_text(outcome, (50, 525), 30, random.choice(color), "monospace")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Black")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
