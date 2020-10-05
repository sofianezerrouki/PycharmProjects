from tkinter import *
from PIL import Image, ImageTk


def showImg(fenetre,x,y,w,h,path):
    load = Image.open(path)
    resize_image = load.resize((w, h), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(resize_image)#make size of image like the origin image


    makeFrame = LabelFrame(fenetre, text="Simple Image From Cifar100", padx=500, pady=620)
    makeFrame.pack()
    inFrame = Label(makeFrame,image = render)
    inFrame.pack()
root = Tk()
showImg(root,30, 30, 480, 600, "2.jpg")
# showImg(340, 20, 300, 200, "moi.jpg")
# showImg(680, 20, 300, 200, "moi.jpg")
# showImg(1020, 20, 300, 200, "moi.jpg")
#
# showImg(10, 240, 300, 200, "moi.jpg")
# showImg(340, 240, 300, 200, "moi.jpg")
# showImg(680, 240, 300, 200, "moi.jpg")
# showImg(1020, 240, 300, 200, "moi.jpg")
#
# showImg(10, 460, 300, 200, "moi.jpg")
# showImg(340, 460, 300, 200, "moi.jpg")


root.state('zoomed')#fullScreen
#showImg(0,0,400,300,"moi.jpg")
# mainloop
root.mainloop()  