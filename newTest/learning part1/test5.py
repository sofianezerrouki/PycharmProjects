from tkinter import *
def hello ():
    myLabel = Label(frame, text="the Button has enterd ...", bg="#1060fa")
    myLabel.place(x=0, y=0)
def dele ():
    myLabel = Label(frame, text="Bla Bla ...", bg="#e2121e")
    myLabel.place(x=0, y=0)
myGui = Tk()
myGui.geometry('500x500+30+30')
frame = Frame(myGui,width=500,height=500)
frame.pack()

myLabel = Label(frame,text="Bla Bla ....",bg="#e2121e",font=("arial",40,"italic"))
myLabel.place(x=0,y=0)
myLabel2 = Label(frame,text="Bla Bla ....",bg="#e2121e").place(x=0,y=22)

myButton = Button(frame,text="Exit",bg="#005400",command=hello,fg="yellow",width="20",font=20).place(x=0,y=45)
myButton2 = Button(frame,text="Delete",bg="#005400",command=dele,fg="yellow",width="20",font=20).place(x=0,y=70)

myGui.mainloop()