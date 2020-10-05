from tkinter import *
import tkinter
from tkinter import messagebox #important

def quitW():
    # tkMessageBox.FunctionName(title, message [, options])
    # showinfo()
    # showwarning()
    # showerror ()
    #askquestion()
    #askokcancel()
    #askyesno()
    #askretrycancel()
    msgValue = messagebox.askyesno("hello","this is your day ")#for yes return 1 for no return -1
    if msgValue==1 :
        fenetre.destroy()

fenetre = Tk()
fenetre.geometry("1000x620+150+50")


barMenu = Menu(fenetre)
fileMenu = Menu(barMenu)

fileMenu.add_command(label="new file")
fileMenu.add_command(label="Message Box")
fileMenu.add_command(label="second")
fileMenu.add_command(label="Quit",command=quitW)

barMenu.add_cascade(label="File",menu = fileMenu)
fenetre.config(menu=barMenu)


fenetre.state('zoomed')#fullScreen
fenetre.mainloop()


#fenetre.attributes("-fullscreen",True)
#fenetre.bind("<Escape>", lambda event: fenetre.attributes("-fullscreen", False))


