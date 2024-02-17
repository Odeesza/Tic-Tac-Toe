from tkinter import *
import numpy as np

def clic(event):
    grid_position = [event.x,event.y]
    print(grid_position)

#Create an instance of tkinter frame or window
win= Tk()

size_of_board = 800
#Create a Label widget

canvas = Canvas(win, width=size_of_board, height=size_of_board)
canvas.pack()
win.bind('<Button-1>', clic)

canvas.create_rectangle(0,0,size_of_board-20,size_of_board-120,fill="blue",outline="black")
for j in range(7):
    for i in range(6):
        canvas.create_oval(10+j*110,10+i*110,110+110*j,110+110*i,fill ="white")

win.mainloop()


