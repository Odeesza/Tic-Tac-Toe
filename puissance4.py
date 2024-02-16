from tkinter import *
import numpy as np


size_of_board = 800
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'

class Puissance_4():
    def __init__(self):
        self.window = Tk()
        self.window.title('Puissance 4')
        self.canvas = Canvas(self.window, width=size_of_board-20, height=size_of_board-120)
        self.canvas.pack()
        # Input from user in form of clicks
        #self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_red_turns = True
        self.board_status = np.zeros(shape=(6, 7))

        self.player_red_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.red_wins = False
        self.blue_wins = False

        self.red_score = 0
        self.blue_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        self.canvas.create_rectangle(0,0,size_of_board-20,size_of_board-120,fill="blue",outline="black")
        for j in range(7):
            for i in range(6):
                self.canvas.create_oval(10+j*110,10+i*110,110+110*j,110+110*i,fill ="white")
    def play_again(self):
        self.initialize_board()
        self.player_red_starts=not(self.player_red_starts)
        self.player_red_turns=self.player_red_starts
        self.board_status = np.zeros(shape=(6, 7))



    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def convert_logical_to_grid_position(self, logical_position):
        logical_position= np.array(logical_position)
        return (size_of_board/3)*logical_position+(size_of_board/6)
        
    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        case = grid_position[0]//100
        for i in range(len(self.board_status[:,case])):
            if self.board_status[5-i,case] == 0:
                return np.array(5-i,case) 

        return np.array(0,case)

    def is_grid_occupied(self,logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True
    def click():

    
game_instance = Puissance_4()
game_instance.mainloop()