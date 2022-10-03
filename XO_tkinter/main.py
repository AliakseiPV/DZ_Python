from cProfile import label
from tkinter import *
import random,time


def win(xo):
    global game
    if ((game[0]==xo and game[1] == xo and game[2] == xo) or\
        (game[3]==xo and game[4] == xo and game[5] == xo)or\
        (game[6]==xo and game[7] == xo and game[8] == xo)or\
        (game[0]==xo and game[3] == xo and game[6] == xo)or\
        (game[1]==xo and game[4] == xo and game[7] == xo)or\
        (game[2]==xo and game[5] == xo and game[8] == xo)or\
        (game[0]==xo and game[4] == xo and game[8] == xo)or\
        (game[2]==xo and game[4] == xo and game[6] == xo)):
        return True
        

def push(middle):
    global game
    global game_left
    global turn
    
    game[middle] = 'X'
    buttons[middle].config(text='X',state="disabled")
    game_left.remove(middle) 

    if middle == 4 and turn == 0:
        computer = random.choice(game_left)
    elif middle != 4 and turn == 0:
        computer = 4

    if turn > 0:       
        computer = 8 - middle
    if computer not in game_left:
        try:
            computer = random.choice(game_left)
        except IndexError: label['text'] = 'Game Over'

    game[computer] = 'O'
    buttons[computer].config(text = 'O', state="disabled")
    if win('X'):
        label['text'] = 'You win!'
    elif win('O'):
        label['text'] = 'You loose!'
    else:
        if(len(game_left) > 1):
            game_left.remove(computer)
        else:
            label['text'] = 'Game Over'



game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text="XO", font=('Arial',20,'bold'),  bg = "blue")

buttons = [Button(width=5,height=2,font=('Arial',28,'bold'), bg="aqua", command = lambda x=i: push(x)) for i in range(9)]


label.grid(row=0,column=0,columnspan=3)
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row,column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0


root.mainloop()