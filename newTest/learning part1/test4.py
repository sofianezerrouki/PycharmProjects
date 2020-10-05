from tkinter import *

W=Tk()
W.geometry("300x300+0+0")

FRAME=Frame(W, width=100, height =50).place(x=200,y=0)

LABEL=Label(FRAME, text="test").pack()

W.mainloop()