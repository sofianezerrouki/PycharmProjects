from tkinter import *

myGui = Tk()
myGui.geometry('500x500+30+30')
frame = Frame(myGui,width=500,height=500)
frame.pack()

myLabel = Label(frame,text="Bla Bla ....",bg="#e2121e").place(x=0 ,y=100)
myLabel2 = Label(frame,text="Bla Bla ....",bg="#e2121e").place(x=0 ,y=140)

myGui.mainloop()