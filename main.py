from game import TicTacToe

def grab_inputs(board):
    """
    Asks for inputs and returns a row, col. Also updates the board state.
    """
    keepasking = True
    while keepasking:
        try:
            row = int(input("Input row"))
            col = int(input("Input column "))
        except (EOFError, KeyboardInterrupt):
            print('Cya nerd')
            exit()
        except:
            print("That's not an integer you mongoloid.")
        
        else: # If it's an int
            valid_board = board.update_board(row, col)
            if valid_board == False:
                print("Your row or col is out of range. Try ranges 0-2 and make sure there's nothing there already.")
            else: # If it's a valid board
                keepasking = False
    return row, col



## The game starts below.
boardgame = TicTacToe()
gameWon = False

while not gameWon:
    boardgame.draw_board()

    # Ask them for a row and column input and updates it once it works.
    row, col = grab_inputs(boardgame)

    player_has_won = boardgame.is_terminal() # Checks if the current player has won.

    # Once the entity added a new piece on the board.
    #gameWon = boardgame.check_victory(row, col)
    random = boardgame.evaluate(gameWon)
    if player_has_won:
        break
    else:
        boardgame.flip_player()
print("Player ", str(boardgame.current_player) + " won!")