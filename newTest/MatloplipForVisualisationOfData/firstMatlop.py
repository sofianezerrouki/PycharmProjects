from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("tkinter Matloplib ")
        self.minsize(640,400)
        self.wm_iconbitmap("icon.ico")
        self.matplotCanvas()
    def matplotCanvas(self):
        f = Figure(figsize=(5,5) )
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,8,9,7,9,5,2])
        canvas = FigureCanvasTkAgg(f,self)
        canvas.get_tk_widget().pack(side= TOP,fill=BOTH,expand=True)
        toolbar= NavigationToolbar2Tk(canvas,self)
        canvas._tkcanvas.pack(side= BOTTOM,fill=BOTH,expand=True)


if __name__ =="__main__":
    root = Root()
    root.mainloop()