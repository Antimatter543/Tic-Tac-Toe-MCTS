from game import TicTacToe

x = TicTacToe()
gameWon = False

while not gameWon:
    x.draw_board()

    # Keep them looped until they give a valid answer to play.
    keepasking = True
    while keepasking:
        try:
            row = int(input("Input row"))
            col = int(input("Input column "))
        except:
            print("That's not an integer you mongoloid.")
        
        else: # If it's an int
            valid_board = x.update_board(row, col)
            if valid_board == False:
                print("Your row or col is out of range. Try ranges 0-2 and make sure there's nothing there already.")
            else: # If it's a valid board
                keepasking = False

    # Once the entity added a new piece on the board.
    gameWon = x.CheckVictory(row, col)
    if gameWon:
        break
    x.flip_player()
print("Player ", str(x.player_turn) + " won!")