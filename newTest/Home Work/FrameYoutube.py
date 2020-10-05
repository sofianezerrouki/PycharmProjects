from tkinter import *

class welcome :



    #constructor
    def __init__(self):
        self.win = Tk()

        self.canvas = Canvas(self.win,width= 800,height=460,bg = "white")
        self.canvas.pack(expand=YES , fill=BOTH)
        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()

        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 460 / 2)
        str1 = "800x460+" + str(x) + "+" + str(y)
        self.win.geometry(str1)


        # disable resize of the window
        self.win.resizable(width=True, height=True)

        self.win.title('WELCOME|PROJECT TITLE |ADMINISTRATOR')

    def add_text(self, t="None ...", x=20, y=20, w=100, h=100):
        text = Label(self,text = t)
        text.place(x=x,y=y,width = w,height= h)



    def add_frame(self,x = 10,y = 10 ,w = 300,h = 300,bg="gray95"):
        # create a inner frame
        self.frame = Frame(self.win, width=w, height=h,bg=bg)
        self.frame.place(x=x, y=y)
        text = Label(self.frame, text="ttttttttttttttt ..........")
        text.place(x=10, y=20, width=90, height=30)


if __name__ == "__main__":

    x = welcome()
    x.add_frame(20,20,755,60)
    x.add_frame(20,90,300,280)
    x.add_frame(350, 90, 100, 280)
    x.add_frame(480, 90, 295, 280)
    x.add_frame(20,380,755,60)
    x.frame.mainloop()

