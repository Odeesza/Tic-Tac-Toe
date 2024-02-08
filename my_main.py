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
        
    def mainloop(self):

    def initialize_board(self):
        

    def play_again(self):
        

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

    def draw_O(self, logical_position):
    
    def draw_X(self, logical_position):
        

    def display_gameover(self):


    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def convert_logical_to_grid_position(self, logical_position):
        
    def convert_grid_to_logical_position(self, grid_position):
        

    def is_grid_occupied(self, logical_position):
    
    def is_winner(self, player):

    
        

    def is_tie(self):


    def is_gameover(self):
        # Either someone wins or all grid occupied





    def click(self, event):
        
game_instance = Tic_Tac_Toe()
game_instance.mainloop()