from tkinter import *
import numpy as np

def clic(event):
    grid_position = [event.x,event.y]
    print(grid_position)

#Create an instance of tkinter frame or window
win= Tk()

size_of_board = 600
#Create a Label widget
label= Label(win, text="Tic-Tac Toe", font= ('Courier 20 underline'))
label.pack()
canvas = Canvas(win, width=size_of_board, height=size_of_board)
canvas.pack()
win.bind('<Button-1>', clic)

for i in range(2):
    canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

for i in range(2):
    canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)
win.mainloop()


