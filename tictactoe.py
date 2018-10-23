#from IPython.display import clear_output
import random
#ALL FUNCTIONS REQUIRED BY THE CODE

#To display the type of board to play
def display_board(board):
    #clear_output()
    print(myboard[1]+' | ' + myboard[2] +' | '+ myboard[3])
    print("---------")
    print(myboard[4]+' | ' + myboard[5] +' | '+ myboard[6])
    print("---------")
    print(myboard[7]+' | ' + myboard[8] +' | '+ myboard[9])

    
#To choose the X or O to by one of the players as a marker
def player_input():
    marker=''
    while not(marker == 'X' or marker == 'O'):
        marker= input("player 1 make you choice in X and O:").upper()

    if marker=='X':
        return ('X','O')
    else:
        return('O','X')

    
#To place the marker at the notified position
def place_marker(board,marker,position):
    board[position]=marker


#To check all the rows , columns and diag for win condition
def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark)or
            (board[4]==mark and board[5]==mark and board[6]==mark)or
            (board[7]==mark and board[8]==mark and board[9]==mark)or
            (board[1]==mark and board[5]==mark and board[9]==mark)or
            (board[7]==mark and board[5]==mark and board[3]==mark))


#To randomly choose which player to start the game
def choose_first():
    
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

    
#To Check if the position choosen is empty or not
def space_check(board,position):
    return board[position]==' '


#To check for the Tie condition
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#player's choice of position to place the marker
def player_choice(board):
    position = 0
    num=[1,2,3,4,5,6,7,8,9]

    while position not in num or not space_check(board,position):
        position = int(input("enter your choice of positon within 1-9 bro:"))

    return position


#To play again 
def replay():
    decision = input("Would you like to play the game again : y or n").lower()
    return decision=='y'


#ACTUAL CODE FOR THE GAME STARTS HERE

#Initial while loop for the replay of game
print("Welcome to Tic Tac Toe Game")
while True:
    #setting up the game
    myboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(myboard)
    player1_marker,player2_marker = player_input()
    turn=choose_first()
    print(turn+" will go first.")
    game = input("would you like to start the game: y or n").lower()
    if game=='y':
        game_on = True
    else:
        game_on = False
    while game_on:
        #PLAYER ONE
        if turn == 'player1':
            display_board(myboard)
            #select position
            position=player_choice(myboard)
            #place mark in the position
            place_marker(myboard,player1_marker,position)
            #check win condition
            if win_check(myboard,player1_marker):
                display_board(myboard)
                print("PLAYER ONE IS THE WINNER")
                game_on=False
            #check Tie condition
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("The Game is a Tie")
                    game_on=False
                
            #no Tie then select next player
                else:
                    turn='player2'
        
        #PLAYER TWO
        else: 
            display_board(myboard)
            #select position
            position=player_choice(myboard)
            #place mark in the position
            place_marker(myboard,player2_marker,position)
            #check win condition
            if win_check(myboard,player2_marker):
                display_board(myboard)
                print("PLAYER TWO IS THE WINNER")
                game_on=False
            #check Tie condition
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("The Game is a Tie")
                    game_on=False
                
            #no Tie then select next player
                else:
                    turn='player1'
    
#end of loop
    if not replay():
        print("Thank You for Playing My Game Dude!")
        break
    

    
