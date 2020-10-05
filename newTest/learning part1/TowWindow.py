import tkinter
from tkinter import *


first = Tk()
second = Tk()

label =Label(text="first").pack()
label2 = Label(second,text="Second").pack()
first.geometry("500x500+10+10")
second.geometry('500x500+600+10')

first.mainloop()