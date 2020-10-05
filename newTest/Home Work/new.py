from tkinter import *

from PIL import Image, ImageTk


class welcome:

    # create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width=990, height=610, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 990 / 2)
        y = int(height / 2 - 700 / 2)
        str1 = "990x610+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=True, height=True)

        # change the title of the window
        self.win.title("WELCOME | PROJECT TITLE | ADMINISTRATOR")

    def add_frame_top(self, x=20, y=20, w=950, h=60, bg="gray95",t = "c"):
        # create a inner frame
        self.frame = Frame(self.win, width=w, height=h, bg=bg)
        text = Label(self.frame, text=t)
        text.place(x=10, y=20)
        self.frame.place(x=x, y=y)

if __name__ == "__main__":
    t="The CIFAR-100 dataset This dataset is just like the CIFAR-10, except it has 100 classes containing 600 images each." \
      " There are 500 training images and 100 testing images per class." \
      " The 100\n classes in the CIFAR-100 are grouped into 20 superclasses." \
      " Each imag\ne comes with a fine label (the\n0 class to which it\n belongs)" \
      "\n and a coarse\n label (the superclass to \nwhich it belongs\n)." \
      "Here \nis the list of classes \nin the \nCIFAR-100"
    x = welcome()
    x.add_frame_top(t = t)
    x.frame.mainloop()