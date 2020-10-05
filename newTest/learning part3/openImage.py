from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

fenetre = Tk()
fenetre.geometry("1300x650+20+20")

def open_file():

    path = filedialog.askopenfilename()
    load = Image.open(path)
    resize_image = load.resize((450, 450), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resize_image)
    myvar = Label(fenetre, image=tkimage,width = 450,height =450)
    myvar.image = tkimage
    myvar.grid(row = 1,column = 0,pady = 30)

frame1 = Frame(fenetre)
frame1.grid(row = 1,column = 1)



#Open le fichier des Images ...
btn1 = Button(frame1,text="Choose Image",font=("tahoma",16),bg="white",fg= "#4065a4",command = open_file)
btn1.pack(expand = YES)
frame1.grid(row = 2,column = 2)

fenetre.mainloop()