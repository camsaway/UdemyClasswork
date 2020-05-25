
#Define Global Variables
P =[0,"","","","","","","","",""]   #Board Poisitions
WINS = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]    #Winning Combinations
PLAYERS = ["","X","O"]        #Player Choices
PLAYER1TURN = False

def clearscreen():
    #I so wish I knew how to do this properly!
    print('\n'*45)

def drawscreen():
    clearscreen()
    print(f'           ')
    print(f'           ')
    print(f'           ')
    print(f'           ')
    print(f'   |   |   ')
    print(f' {P[7]} | {P[8]} | {P[9]} '+'                    7   8   9')
    print(f'   |   |   ')
    print(f'-----------')
    print(f'   |   |   ')
    print(f' {P[4]} | {P[5]} | {P[6]} '+'                    4   5   6')
    print(f'   |   |   ')
    print(f'-----------')
    print(f'   |   |   ')
    print(f' {P[1]} | {P[2]} | {P[3]} '+'                    1   2   3')
    print(f'   |   |   ')
    print(f'           ')

def getmove():
    #Need to get input and return a valid move position and set the global P token
    
    global P, PLAYERS
    
    validmove = False
    while validmove == False:
        move = input('Where do you want to play? (1-9)')[0]
        if move in '123456789':
            move=int(move)
            if P[move] == " ":
                validmove = True
            else:
                print('That square already taken, please try again.')
        else:
            print('Invalid entry, please try again using the numbers 1 through 9.')
    
    if PLAYER1TURN:
        P[move] = PLAYERS[1]
    else:
        P[move] = PLAYERS[2]
        
    return move
    
def checkwin(play):
    #play should be the position (1-9) that was just completed
    #needs to return true if there is now a winning combination
    
    global WINS, P

    for win in range (0,len(WINS)):
        if play in WINS[win]:
            if P[WINS[win][0]] == P[WINS[win][1]] == P[WINS[win][2]]:
                return True
    
    return False

def init():
    #Reset the board for a new game
    print('\nInitialising...\n')
    global P, PLAYERS, PLAYER1TURN
    P[1] = " "
    P[2] = " "
    P[3] = " "
    P[4] = " "
    P[5] = " "
    P[6] = " "
    P[7] = " "
    P[8] = " "
    P[9] = " "
    PLAYERS[1] = "X"
    PLAYERS[2] = "O"
    PLAYER1TURN = False
    PLAYERS[1] = input('Player 1, do you want to be X or O?', )[0].upper()
    if PLAYERS[1] == 'X':
        PLAYERS[2] = 'O'
    else:
        PLAYERS[1] = 'O'
        PLAYERS[2] = 'X'

def playgame():
    
    global PLAYER1TURN

    bolPlay = True
    while bolPlay:
        if input('Would you like to play a new game of Tic Tac Toe? (Y/N)')[0].upper() == "Y":
            init()
            for turn in range(1,10):
                PLAYER1TURN = not(PLAYER1TURN) #Initialisation sets this to false so we need to change as part of the first turn
                drawscreen()
                if PLAYER1TURN:
                    print('Player 1')
                else:
                    print('Player 2')
                move = getmove()
                drawscreen()
                bolWin = checkwin(move)
                if bolWin:
                    if PLAYER1TURN:
                        print(' ')
                        print('**************************************')
                        print('* Congratulations Player 1, you win! *')
                        print('**************************************')
                        print(' ')
                        print(' ')
                    else:
                        print(' ')
                        print('**************************************')
                        print('* Congratulations Player 2, you win! *')
                        print('**************************************')
                        print(' ')
                        print(' ')
                    break
                    
            if not(bolWin):
                print(' ')
                print('Sorry, looks like it was a draw.')
                print(' ')
                print(' ')
 
        else:
            bolPlay = False
            
    print('Thanks for playing!')
        
playgame()
