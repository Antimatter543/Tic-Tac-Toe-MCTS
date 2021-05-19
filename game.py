# We'll use the time module to measure the time of evaluating
# game tree in every move. It's a nice way to show the
# distinction between the basic Minimax and Minimax with
# alpha-beta pruning :)
import time
import numpy as np

HUMAN = +1 
BOT = -1

class TicTacToe:
    def __init__(self):
        """
        Player is 1, enemy is -1. In hindsight, I should've made these constants HUMAN, COMP or something but oh well.
        """
        self.board = np.zeros((3,3))

        # Player X always plays first
        self.current_player = HUMAN # We are 1, Enemy is -1. Human starts first.

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
            self.board[row][col] = self.current_player
            return True
        
        return False


    
    def is_terminal(self) -> bool:
        """
        Uses board and player to see if that player won.
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :return: True if the player wins
        """
        state = self.board
        player = self.current_player
        win_states = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
        ]

        if [player, player, player] in win_states:
            return True
        else:
            return False

    

    def flip_player(self):
        # Changes player turn.
        if self.current_player == HUMAN:
            self.current_player = BOT
        else:
            self.current_player = HUMAN
    

    ##### BEGIN MINIMAX STUFF #####
    ###############################


    def empty_cells(self) -> list:
        """
        Returns list of empty cells in board, O(n^2) as tuples [(x,y),(x,y),...]
        """
        empty_cells = []
        for row in self.board:
            # rows
            for col in row:
                #col in row therefore x,y -> [row][col].
                if self.board[row][col] == 0:
                    empty_cells.append((row, col))

    def evaluate(self) -> int:
        """
        Returns int 1 or -1 based on if computer won (1 if it did).
        Says good job! if computer wins, and bad job if not (by +1 or -1).
        """
        current_player = self.current_player
        if self.is_terminal():
            # Checks who wins and assigns score from there.
            if current_player == HUMAN: # If human win
                score = -1

            elif current_player == BOT:
                score = 1

            else:
                score = 0
        return score
    
    def minimax(self, depth, maximisingPlayer):
        if depth == 0 or self.is_terminal(self):
            score = self.evaluate(self)

        if maximisingPlayer:
            value = -np.Infinity
            for child in self.empty_cells(self):
                value = max(value, self.minimax(child, depth-1, not maximisingPlayer)) # This line might be wrong btw. (Maximising might be False).
        
        else: #minimising player
            value = np.Infinity
            for child in self.empty_cells(self):
                value = min(value, self.minimax(child, depth-1, maximisingPlayer)) #Might be wrong (maximising might just be True)

        return value