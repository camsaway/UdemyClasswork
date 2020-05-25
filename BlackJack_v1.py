'''
Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! 
'''

'''
My first attempt at an OOP BlackJack game in Python
'''
from random import randrange

class Card():
    '''
    This object represents a single playing card
    '''
    
    def __init__(self, suit, face): # Suit and Face to be strings either 9-10 or start with K(ing), Q(ueen), J(ack) or A(ce)
        self.suit = str(suit)
        self.face = str(face)
        self.ace = False
        if self.face in ['J', 'Q', 'K']:
            self.value = 10
        elif self.face == 'A':
            self.value = 11
            self.ace = True
        else:
            self.value = int(self.face)
        #Am not applying error checking as the parameters for the object will be provided by code not user
        
    def FlipAce(self):
        if self.ace:
            if self.value == 11:
                self.value = 1
            else:
                self.value =11

class Shoe():
    '''
    An object to represent the Shoe full of cards
    '''
    
    def __init__(self, decks = 1): #Option to provide a decks parameter to create a shoe with more than 1 deck of cards (casino's typically use 6 to 8 decks in a shoe)
        self.cards = []
        for deck in range(decks):
            for suit in ['H', 'D', 'S', 'C']:
                for face in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                    card = Card(suit,face)
                    self.cards.append(card)
                    
    def DrawCard(self):
        if len(self.cards) == 0:
            print("We have run out of cards!!!")
        else:
            rnd = randrange(len(self.cards))
            card = self.cards[rnd]
            del self.cards[rnd]
            return card
        
    def __len__(self):
        return len(self.cards)

class Hand():
    '''
    This object is to represent a players hand. It could be the dealer or a player.
    '''
    
    def __init__(self):
        self.value = 0
        self.ace_11s = 0
        self.cards_in_hand = []
        self.bust = False
        self.bet = 0
        
    def addcard(self, newcard): #newcard should be of object type Card
        self.cards_in_hand.append(newcard)
        self.value += newcard.value
        if newcard.face == 'A':
            self.ace_11s += 1
        
        if self.value > 21:     #Check for bust and flipping aces if needed
            self.bust = True
            if self.ace_11s > 0:
                self.value -= 10
                self.ace_11s -= 1
                self.bust = False
    
    def display(self):
        mystr = ""
        if self.bet != 0:
            mystr = "Bet R" + str(self.bet) + " "
        for card in self.cards_in_hand:
            mystr = mystr + " [ " + card.face + card.suit +" ]"
        return mystr
        
    def displayvalue(self):
        if self.ace_11s == 0:
            return str(self.value)
        else:
            return str(self.value-10) + ' or ' + str(self.value)
            

class Player():
    '''
    Representation of a Player. Not relevant to dealer
    '''
    
    def __init__(self, name, buyin = 500):
        self.name = name
        self.balance = buyin
        self.hand = Hand()

def clearscreen():
    #I so wish I knew how to do this properly!
    print('\n'*45)

def drawscreen(hidedealercard=True,message="",question=""):
    clearscreen()
    print(f'Player: {player1.name} (R{player1.balance})')
    print(player1.hand.display())
    print('')
    print('') 
    print('Dealer:')
    if hidedealercard:
        print(' [ ** ]'+dealer.hand.display()[7:])
    else:
        print(dealer.hand.display())
    print('') 
    print('') 
    print('') 
    print('') 
    print(message)
    print('') 
    if question != "":
        return input(question)
    else:
        print('')

def playhand():

    # Reset hands
    player1.hand = Hand()
    dealer.hand = Hand()

    ##Get Bet
    good_bet = False
    message = ""
    while not good_bet:
        try:
            bet = int(drawscreen(False, message, "Player 1: How much would you like to bet? "))
            if bet <= player1.balance:
                good_bet = True 
            else:
                message = "*** Sorry you only have R"+str(player1.balance)+"***"
        except:
            message = "*** Please enter only numbers ***"
    player1.hand.bet = bet
    player1.balance -= bet
    
    ##Deal Cards
    player1.hand.addcard(our_deck.DrawCard())
    player1.hand.addcard(our_deck.DrawCard())
    dealer.hand.addcard(our_deck.DrawCard())
    dealer.hand.addcard(our_deck.DrawCard())
    
    ## Hit or Stand? (Player)
    while player1.hand.value < 21:
        optbad = True
        while optbad:
            opt = drawscreen(True,'Player 1: your current score is '+player1.hand.displayvalue(),"(H)it or (S)tand? ")[0].upper()
            if opt in ['H', 'S']:
                optbad = False
        if opt=="S":
            break
        else:
            player1.hand.addcard(our_deck.DrawCard())

    ## Dealer cards - use delay, also think about drawing to at least 16
    if player1.hand.value <= 21:
        while dealer.hand.value < 16:
            dealer.hand.addcard(our_deck.DrawCard())
    
    ## Decide Bust, Blackjack, Push or Win
    result = 'Unknown'
    payout = player1.hand.bet
    if player1.hand.value > 21:
        result = 'Sorry you Bust'
        payout *= 0
    elif player1.hand.value == 21 and len(player1.hand.cards_in_hand) == 2:
        result = 'Blackjack!!'
        payout *= 2.5
        if dealer.hand.value == 21 and len(dealer.hand.cards_in_hand) == 2:
            result = 'Blackjack!  But the dealer also has Blackjack so push.'
            payout *= 1
    elif player1.hand.value > dealer.hand.value:
        result = "You won"
        payout *= 2
    elif dealer.hand.value > 21:
        result = "You won"
        payout *= 2
    elif player1.hand.value == dealer.hand.value:
        result = 'Push'
        payout *= 1
    else:
        result = 'Sorry, you lost.'
        payout *= 0
    
    ## Settle Bet
    player1.balance += payout

    return [result, payout]
    
if __name__ == '__main__':
    our_deck = Shoe()
    clearscreen()
    player1 = Player(input('What is your name? '))
    dealer = Player('Dealer')
    play = True
    while play:
        result = playhand()
        if len(our_deck.cards) < 17:
            our_deck = Shoe()
            result[0] += ' ***JUST RESCHUFFLED*** '
        play = drawscreen(False,result[0]+' Paid out: R'+str(result[1]),"Would you like to play again (y/n)? ")
        if play[0].upper() != 'Y':
            play = False
