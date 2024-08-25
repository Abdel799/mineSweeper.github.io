import random
import re
"""
Created on Fri Aug 23 18:16:52 2024

@author: abdelrahmanabdelaal
"""


class Board:
    def __init__(self, dimension_size, num_bombs):
        
        # dimension size
        self.dimension_size = dimension_size
        
        # number of bombs
        self.num_bombs = num_bombs
        
        # creating the board
        self.board = self.make_new_board()
        self.assign_values_to_board()
        
        # initialize a set to keep track of which spots are uncovered
        # this set will include (row,col) tuples
        
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    
    def make_new_board(self):
        
        # generating a new board
        board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        
        # [[None, None, ..., None]
        # [None, None, ..., None]
        # [None, None, ..., None]]
        
        # planting the bombs
        bombs_planted = 0
        
        while bombs_planted < self.num_bombs:
            location = random.randint(0, self.dimension_size**2 - 1)
            row = location // self.dimension_size      # calculating row
            column = location % self.dimension_size    # calculating col
            
            if board[row][column] == '*':
                # this means we've already planted a bomb here
                continue
            
            board[row][column] = '*'
            bombs_planted += 1
        
        return board
    
    
      
    def assign_values_to_board(self):
        
        # assigning values 0 - 9 to locations on the board that are not bombs
        
        for row in range (self.dimension_size):
            
            for column in range (self.dimension_size):
                
                if self.board[row][column] == '*':
                    continue
                
                self.board[row][column] = self.get_num_neighboring_bombs(row, column)
    
    
    
    
    def get_num_neighboring_bombs(self, row, column):
        # iterate through each of the neighboring positions and sum number of bombs
        
        # top left: (row-1, col-1)
        
        # top middle: (row-1, col)
        
        # top right: (row-1, col+1)
        
        # left: (row, col-1)
        
        # right: (row, col+1)
        
        # bottom left: (row+1, col-1)
        
        # bottom middle: (row+1, col)
        
        # bottom right: (row+1, col+1)
         
        num_neighboring_bombs = 0
        
        for r in range (max(0, row-1), min(self.dimension_size-1, row+1) + 1):        # checking below and above current row
            
            for c in range(max(0, column-1), min(self.dimension_size-1, column+1) + 1):     # checking to the right and left of current column
                
               if r == row and c == column:
                   continue # don't check our current location
            
               if self.board[r][c] == '*':
                   num_neighboring_bombs += 1
        
        return num_neighboring_bombs
    
    
    
    def dig(self, row, column):
        # dig at location
        # return True if successful dig, False if bomb dug
        
        # 1. hit a bomb -> game over
        # 2. dig at location with neighboring bombs -> finish dig
        # 3. dig at location with no neighboring bombs -> recursively dig neighbors
        
        self.dug.add((row, column)) # keeps track that we dug here
        
        
        if self.board[row][column] == '*':
            return False
        
        elif self.board[row][column] > 0:
            return True
        
        # is self.board[row][column] == 0
        for r in range (max(0, row-1), min(self.dimension_size-1, row+1) + 1):        # checking below and above current row
            
            for c in range(max(0, column-1), min(self.dimension_size-1, column+1) + 1):     # checking to the right and left of current column
        
                if (r,c) in self.dug:
                    continue
                
                self.dig(r,c)
        
        return True
    
    
    def __str__(self):
        # prints out the board
        
        visible_board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        
        for row in range(self.dimension_size):
            
            for col in range (self.dimension_size):
                
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                
                else:
                   visible_board[row][col] = ' ' 
        
        string_rep = ''
        
        widths = []
        
        for idx in range(self.dimension_size):
           columns = map(lambda x: x[idx], visible_board)
           widths.append(
               len(
                   max(columns, key = len)
               )
           )
        
        
        
        
        indices = [i for i in range(self.dimension_size)]
        indices_row = '   '
        cells = []
        
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
            
        indices_row += '  '.join(cells)
        
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
                
            string_rep += ' |'.join (cells)
            string_rep += ' |\n'
            
            
        str_len = int(len(string_rep) / self.dimension_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len
        
        
        return string_rep
        
        


# play the game
def play(dimension_size = 10, num_bombs = 10):
    
    # create the board & plant bombs
    board = Board(dimension_size, num_bombs)
    
    safe = True
    
    while len(board.dug) < board.dimension_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1]) 
        
        if row < 0 or row >= board.dimension_size or col < 0 or col >= dimension_size:
            print("Invalid loction. Try again!")
            continue
        
        # if user input is valid, we DIG
        safe = board.dig(row, col)
        
        if not safe:
            # dug a bomb NAHHH
            break # GAME OVER
    
    if safe:
        print("CONGRATS YOU WON")
    
    else:
        print("Game over sry ")
        
        board.dug = [(r,c) for r in range(board.dimension_size) for c in range (board.dimension_size)]
        print(board)
    

play()
    
    
    
    
    
    
    
    
    