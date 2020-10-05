from tkinter import *
fenetre = Tk()

fenetre['bg']='white'
fenetre.state("zoomed")
# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.place(10,10,600,600)
Frame1.pack(side=TOP, padx=30, pady=30)
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
fenetre.mainloop()

