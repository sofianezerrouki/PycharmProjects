from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from skimage import io , color
from skimage import data
from skimage.color import rgb2hsv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np

def previousImage():
    i = 1
def nextImage():
    i = 2

def open_file():
    #path = filedialog.askopenfilename()
    path ="C:/Users/Sof/Jupyter Files/images-for-testing/cat2.jpg" #lazem ndrak 3la lboutton bach tban l image 
    load = Image.open(path)
    resize_image = load.resize((450, 450), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resize_image)
    myvar = Label(fenetre, image=tkimage,width = 450,height =450)
    myvar.image = tkimage
    myvar.grid(row = 1,column = 0,pady = 30)
    
def HSV():
    path ="C:/Users/Sof/Jupyter Files/images-for-testing/cat2.jpg" 
    rgb_img = mpimg.imread(path)

    hsv_img = rgb2hsv(rgb_img)
    hue_img = hsv_img[:, :, 0]
    satur_img = hsv_img[:, :, 1]
    value_img = hsv_img[:, :, 2]
    
    ax1 = plt.subplot2grid((1, 3), (0,0)).imshow(hue_img)
    ax2 = plt.subplot2grid((1, 3), (0,1)).imshow(satur_img)
    ax3 = plt.subplot2grid((1, 3), (0,2)).imshow(value_img)
    myvar = Label(fenetre, image=value_img,width = 450,height =450)
    myvar.image = value_img
    myvar.grid(row = 1,column = 0,pady = 30)
    
def RGB():
    path ="C:/Users/Sof/Jupyter Files/images-for-testing/cat2.jpg"
    
    figure=Figure(figsize=(5,5),dpi=100)  
     
def LUV():
    tkimage = color.rgb2hsv(tkimage)
    myvar = Label(fenetre, image=tkimage,width = 450,height =450)
    myvar.image = tkimage
    myvar.grid(row = 1,column = 0,pady = 30)
def LAB():
    tkimage = color.rgb2hsv(tkimage)
    myvar = Label(fenetre, image=tkimage,width = 450,height =450)
    myvar.image = tkimage
    myvar.grid(row = 1,column = 0,pady = 30)
def YUV():
    tkimage = color.rgb2hsv(tkimage)
    myvar = Label(fenetre, image=tkimage,width = 450,height =450)
    myvar.image = tkimage
    myvar.grid(row = 1,column = 0,pady = 30)   
    
def predict():
        
    path ="C:/Users/Sof/Jupyter Files/images-for-testing/cat2.jpg"
    print("This is a : ")
    
    

fenetre = Tk()
fenetre.title("Predector Using Cifar100")
fenetre.config(background="#4065a4")
fenetre.geometry("1300x650+20+20")
    
labal1 = Label(fenetre,text = "Getting a Directory Listing To Cifar100",font=("arial",25),bg= "#989898",fg="white")
labal1.grid(row = 0,column = 0 , columnspan = 2,padx = 5,pady = 2)

frame1 = Frame(fenetre,bg="#989898")
frame1.grid(row = 1,column = 1)



#Open le fichier des Images ...
btn1 = Button(frame1,text="Choose Image",font=("tahoma",16),bg="white",fg= "#4065a4",command = open_file)
btn1.pack(expand = YES)
frame1.grid(row = 2,column = 2)
#frame 3
frame3 = Frame(fenetre,bg="#4065a4")

label = Label(frame3,text = "Open an Image",pady = 220,padx = 200,fg = "#ffffff",bg="#4f65aa")
label.pack(expand=YES,padx=100)

frame3.grid(row = 1,column = 0,pady = 30)

#frame 5
frame5 = Frame(fenetre,bg="#4065a4")
label = Label(frame5,text = "Convert To ",pady = 10,padx = 10,font=("tahoma",20),fg = "#ffffff",bg="#4f65aa")
label.grid(row= 0,column = 0 ,padx = 40,pady=10)               
btn5 = Button(frame5,text="HSV",font=("tahoma",16),bg="white",fg= "#4065a4",command = HSV)
btn5.grid(row= 1,column = 0 ,padx = 40,pady=10)
btn6 = Button(frame5,text="LUV",font=("tahoma",16),bg="white",fg= "#4065a4",command = LUV)
btn6.grid(row= 2,column = 0 ,padx = 40,pady=10)
btn7 = Button(frame5,text="RGB",font=("tahoma",16),bg="white",fg= "#4065a4",command = RGB)
btn7.grid(row= 3,column = 0 ,padx = 40,pady=10)
btn8 = Button(frame5,text="LAB",font=("tahoma",16),bg="white",fg= "#4065a4",command = LAB)
btn8.grid(row= 4,column = 0 ,padx = 40,pady=10)
btn9 = Button(frame5,text="YUV",font=("tahoma",16),bg="white",fg= "#4065a4",command = YUV)
btn9.grid(row= 5,column = 0 ,padx = 40,pady=10)
frame5.grid(row = 1,column = 2,pady = 30)

#frameButtom
frameButtom = Frame(fenetre,bg="#4065a4")

btn2 = Button(frameButtom,text="<<",font=("tahoma",16),bg="white",fg= "#4065a4",command = previousImage)
btn2.grid(row= 0,column = 0 ,padx = 60,pady=35)

btn3 = Button(frameButtom,text=">>",font=("tahoma",16),bg="white",fg= "#4065a4",command = nextImage)
btn3.grid(row= 0,column = 1 ,padx = 60,pady=35)

frameButtom.grid(row = 2,column = 0)
#frame4
frame4 = Frame(fenetre,bg="#4065a4")
btn1 = Button(frame4,text="Get Class",font=("tahoma",16),bg="white",fg= "#4065a4",command = predict)
btn1.pack(expand = YES)
label = Label(frame4,text = "This is a : ",pady = 120,padx = 1,font=("tahoma",60),fg = "#ffffff",bg="#4f65aa")
label.pack(expand=YES)
frame4.grid(row = 1,column =1,pady=30)

#afficher la fenetre
fenetre.mainloop()