from tkinter import *
from tkinter import colorchooser

fenetre = Tk()
color = colorchooser.askcolor()

def choose():
    c= colorchooser.askcolor()
    label = Label(fenetre, text="your color ",bg=c[1])
    label.pack()
button = Button(text="Choose Color",command= choose)

button.pack()
fenetre.mainloop()