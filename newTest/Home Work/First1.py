from tkinter import *
import webbrowser

def open_youtube_chanel():
    webbrowser.open_new("https://www.youtube.com/user/Gravenilvectuto")

window = Tk()
window.title("First1")
window.iconbitmap("icon.ico")
window.config(background="#00C853")
window.geometry("1300x660+10+10")
window.minsize(700,500)
#création d'un Frame
frame = Frame(window,bg="#00C853")#bd => Bordure , relief => help
#Ajout d'un text (Label)
text = Label(
            frame,
            text = "Cifar100 and Cifar10 ...",
            font = ("Courrier",40),
            bg ="#00C853",
            fg = "#ffffff"
            )
text.pack()
#Ajout d'un sub_text (Label)
sub_text = Label(
            frame,
            text = "Theme 2 Blue is used as the primary color for areas of the app ",
            font = ("Courrier",25),
            bg ="#00C853",
            fg = "#ffffff"
            )
sub_text.pack()
#Ajout d'une Button
btn = Button(frame,text = " Open Youtube ",font=("Tahoma",25),bg = "#FFFFFF",fg="#00C853",
             command = open_youtube_chanel)#l'appel de ffonction : sons parentaise .
btn.pack(pady = 30,fill = X)


#placer le Frame
frame.pack(expand = YES)
#afficher la fenetre
window.mainloop()