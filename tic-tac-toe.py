#------global variable------
#game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if game is still going
game_still_going = True

#who won? or tie?
winner = None


#whos turn is it? 
current_player = "X"


#display board
def display_board():
  print(board[0] + " | " + board[1] + " | " +board[3])
  print(board[3] + " | " + board[4] + " | " +board[5])
  print(board[6] + " | " + board[7] + " | " +board[8])
  

#Play a game of tic tac toe
def play_game():
  
  
  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:

    #handle a single turn of an arbitrary player
    handle_turn(current_player)
    

    #check if the game has ended
    check_if_game_over()

    
    #flip to the other player
    flip_player()
    

  #The game has ended
  if winner ++ "X" or winner == "0":
    print(winner + "won!")
  elif winner == None: 
    print("Tie")


#handle a single turn of an arbitrary player
def handle_turn(player):
  position = input("Choose a position from 1-9: ")
  position = int(position) - 1

  board[position] = "X"
  
  display_board()



def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  #check rows
  #check collums
  #check diagonals
  return

def check_rows():
  return

def check_columns():
  return

def check_diagonals():
  return



def check_if_tie():

  #
  #
  #
  return


def flip_player():

  return




play_game()





#board
#display board
#play game
#handle turn
#check win
  #check rows
  #check collumns
  #check diaganols
#check tie
#flip player
