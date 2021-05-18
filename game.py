# We'll use the time module to measure the time of evaluating
# game tree in every move. It's a nice way to show the
# distinction between the basic Minimax and Minimax with
# alpha-beta pruning :)
import time
import numpy as np

class TicTacToe:
    def __init__(self):
        """Player is 1, enemy is -1."""
        self.board = np.zeros((3,3))

        # Player X always plays first
        self.player_turn = 1 # We are 1, Enemy is 2.

    def draw_board(self):
        print(self.board)

    def is_valid(self, board, row, col):
        """
        Checks if the rows and columns are valid and not already taken
        """
        if (0 <= row <=2) and (0<= col <=2):
            if board[row][col] == 0:
                return True
        return False
 

    def update_board(self, row, col):
        """
        Checks if position on board is valid and updates the board based on the current player turn
        """
        if self.is_valid(self.board, row, col):
            self.board[row][col] = self.player_turn
            return True
        
        return False

    def CheckVictory(self, x, y):
        board = self.board
        #check if previous move caused a win on vertical line  -> Checks if they are equivalent for first column.
        if board[0][y] == board[1][y] == board [2][y]:
            return True

        #check if previous move caused a win on horizontal line 
        if board[x][0] == board[x][1] == board [x][2]:
            return True

        #check if previous move was on the main diagonal and caused a win
        if x == y and board[0][0] == board[1][1] == board [2][2]:
            return True

        #check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
            return True

        return False         
    

    def flip_player(self):
        # Changes player turn.
        if self.player_turn == 1:
            self.player_turn = -1
        else:
            self.player_turn = 1

# x = TicTacToe()

# gameWon = False
# while not gameWon:
#     x.draw_board()

#     # Keep them looped until they give a valid answer to play.
#     keepasking = True
#     while keepasking:
#         try:
#             row = int(input("Input row"))
#             col = int(input("Input column "))
#         except:
#             print("That's not an integer you mongoloid.")
        
#         else: # If it's an int
#             valid_board = x.update_board(row, col)
#             if valid_board == False:
#                 print("Your row or col is out of range. Try ranges 0-2 and make sure there's nothing there already.")
#             else: # If it's a valid board
#                 keepasking = False

#     # Once the entity added a new piece on the board.
#     gameWon = x.CheckVictory(row, col)
#     if gameWon:

#         break
#     x.flip_player()
# print("Player ", str(x.player_turn) + " won!")