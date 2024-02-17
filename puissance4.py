from tkinter import *
import numpy as np


size_of_board = 800
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_red_color = '#EE4035'
symbol_blue_color = '#0492CF'
Green_color = '#7BC043'

class Puissance_4():
    def __init__(self):
        self.window = Tk()
        self.window.title('Puissance 4')
        self.canvas = Canvas(self.window, width=size_of_board-20, height=size_of_board-120)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

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
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

    def draw_blue(self, logical_position):
        #grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(10+logical_position[1]*110,10+logical_position[0]*110,110+110*logical_position[1],110+110*logical_position[0],fill =symbol_blue_color)
    
    def draw_red(self, logical_position):
        #grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(10+logical_position[1]*110,10+logical_position[0]*110,110+110*logical_position[1],110+110*logical_position[0],fill =symbol_red_color)





    def display_gameover(self):
        if self.red_wins:
            self.red_score +=1
            text = "Player red wins"
            cool_text = "gg pd"
            color = symbol_red_color
        elif self.blue_wins:
            self.blue_score +=1
            text = "Player blue wins"
            cool_text = "gg pd"
            color = symbol_blue_color
        else:
            self.tie_score+=1
            text = "It's a tie"
            cool_text = ""
            color = "gray"

        self.canvas.delete("all")

        self.canvas.create_text(size_of_board/2,size_of_board/3,font =  ('Helvetica', '50'),text = text, fill = color)
        self.canvas.create_text(100,165,angle=30,text=cool_text,font=("Times","25"),fill = "blue")

        self.canvas.create_text(size_of_board/2,size_of_board*2/3,font = ("Times","30") ,text = "Scores:\n", fill = "green")
        
        score_text = 'Player red : ' + str(self.red_score) + '\n'
        score_text += 'Player blue: ' + str(self.blue_score) + '\n'
        score_text += 'Tie: ' + str(self.tie_score)
        self.canvas.create_text(size_of_board/2,3*size_of_board/4,font = ("Times","20") ,text = score_text, fill = "green")
        score_text = "Click to play again\n"
        self.canvas.create_text(size_of_board/2,11*size_of_board/12,font = ("Times","15") ,text = score_text, fill = "gray")
        
        self.reset_board = True


    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

        
    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        col = grid_position[0]//110
        for i in range(len(self.board_status[:,col])):
            if self.board_status[5-i,col] == 0:
                return np.array([5-i,col]) 

        return np.array([0,col])

    def is_grid_occupied(self,logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True



    def check_sequence(self,arr, sequence):
        for i in range(len(arr) - len(sequence) + 1):
            subarray = arr[i:i+len(sequence)]
            if np.array_equal(subarray, sequence):
                return True
        return False

    def is_winner(self,player):

        player = -1 if player == 'red' else 1
        
        sequence = np.array([player,player,player,player])
        #Horizontals
        for j in range(6):
            h = np.array(self.board_status[5-j,:])
            if self.check_sequence(h,sequence):
                return True
            
        #Verticals
        for i in range(7):
            h = self.board_status[:,i]
            if self.check_sequence(h,sequence):
                return True 
            
        #diagonals
        for i in range(-2,4):
            d1 = np.diag(self.board_status,i)
            d2 = np.fliplr(self.board_status).diagonal(i)
            if self.check_sequence(d1,sequence) or self.check_sequence(d2,sequence):
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
        self.red_wins = self.is_winner('red') #True or False
        if not self.red_wins:
            self.blue_wins = self.is_winner('blue') #True or False

        if not self.blue_wins:
            self.tie = self.is_tie() #True or False

        gameover = self.red_wins or self.blue_wins or self.tie #si il y a un True => True

        if self.red_wins:
            print('Red wins')
        if self.blue_wins:
            print('Blue wins')
        if self.tie:
            print('Its a tie')

        return gameover
        
    

    def click(self,event):
        grid_position = [event.x,event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)
        if not(self.reset_board):
            if self.player_red_turns:
                if not(self.is_grid_occupied(logical_position)) :
                    self.draw_red(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_red_turns=not(self.player_red_turns)
            else:
                if not(self.is_grid_occupied(logical_position)):
                    self.draw_blue(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_red_turns=not(self.player_red_turns)
            #Check if it's gameover
            if self.is_gameover():
                self.display_gameover()
        else:#Play again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False
    
game_instance = Puissance_4()
game_instance.mainloop()