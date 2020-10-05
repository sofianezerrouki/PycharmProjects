import string
from tkinter import *
from random import randint, choice


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password ="".join( choice(all_chars) for c in range(randint(password_min,password_max)))
    passwordEntry.delete(0,END)
    passwordEntry.insert(0,password)

window = Tk()
window.geometry("1200x540")
window.title('Password Generater ')
window.iconbitmap("2.ico")
window.config(background="#4065A4")
#création d'un Frame
frame = Frame(window,bg="#4065A4")
#Création d'une Image
width = 300
height = 300
image = PhotoImage(file="cookie.png").zoom(10).subsample(20)# Canvas d'ont support l'extension icon and jpej
canvas = Canvas(frame,width=width,height=height,bg="#4065A4",highlightthickness=0)#Canvzs : c'est un espace qu'on va déssiner des composent graphique (image,text,triangle ....)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row = 0 ,column = 0,sticky = W)
#sub Frame
rightFrame = Frame(frame,bg='#4065a4')


#Création de text
text = Label(rightFrame,text = "Mot De Passe ",font = ("tahoma",32),bg = "#4065A4",fg = "white")
text.pack(padx = 10,pady = 10)
#Password Entry
passwordEntry = Entry(rightFrame,font = ("tahoma",32),bg = "#4065A4",fg = "white")
passwordEntry.pack(padx = 10,pady = 10)
#Création un Button
btnGenerer = Button(rightFrame,text = "Générer",font = ("tahoma",32),bg = "#4065A4",
                    fg = "white",command = generate_password)
btnGenerer.pack(padx = 10,pady = 10,fill =X)
rightFrame.grid(row = 0 , column = 1,sticky = W)

#ToP Frame
topFrame = Frame(window,bg='#00BFA5')
#Création de text
text = Label(topFrame,text = "Mot De Passe ",font = ("tahoma",32),bg = "#00BFA5",fg = "white")
text.pack(padx = 10,pady = 10)

#Création un Button
btnGenerer = Button(topFrame,text = "Générer ",width =60,font = ("tahoma",32),bg = "#ffffff",
                    fg = "#00BFA5",command = generate_password)
btnGenerer.pack(padx = 10,pady = 10,fill =X)
topFrame.grid(row = 0 , column = 0,sticky = W)

#placer le Frame
frame.grid(row = 1 , column = 0,sticky = W)
#Menu
menuBar = Menu(window)
#premiere menu
fileMenu = Menu(menuBar,tearoff = 0)
fileMenu.add_command(label = "New Project")
fileMenu.add_command(label = "New ...")
fileMenu.add_command(label = "Open Project")
fileMenu.add_command(label = "Exit",command = window.quit)

#add file Menu to menu Bar
menuBar.add_cascade(label="File ",menu = fileMenu)
#add menu bar to window
window.config(menu = menuBar)

#afficher la fenetre
window.mainloop()