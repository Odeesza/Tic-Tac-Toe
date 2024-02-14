# Author: aqeelanwar
# Created: 12 March,2020, 7:06 PM
# Email: aqeel.anwar@gatech.edu

from tkinter import *
import numpy as np


size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class Tic_Tac_Toe():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0
    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    #def play_again(self):
        

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

    #def draw_O(self, logical_position):
    
    #def draw_X(self, logical_position):
        

    #def display_gameover(self):


    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    #def convert_logical_to_grid_position(self, logical_position):
        
    #def convert_grid_to_logical_position(self, grid_position):
        

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True
    
    def is_winner(self, player):
        player = -1 if player == 'X' else 1
    
        # 3 in a row
        for i in range(3):
            if self.board_status[i][0]==self.board_status[i][1]==self.board_status[i][2] == player:
                return True
            elif self.board_status[0][i]==self.board_status[1][i]==self.board_status[2][i] == player:
                return True
        # diagonals
        for i in range(3):
            if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                return True
            elif self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                return True
        
        return False

    
        

    def is_tie(self):

        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie
    
    def is_gameover(self):
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X') #True or False
        if not self.X_wins:
            self.O_wins = self.is_winner('O') #True or False

        if not self.O_wins:
            self.tie = self.is_tie() #True or False

        gameover = self.X_wins or self.O_wins or self.tie #si il y a un True => True

        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins')
        if self.tie:
            print('Its a tie')

        return gameover





    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)


game_instance = Tic_Tac_Toe()
game_instance.mainloop()