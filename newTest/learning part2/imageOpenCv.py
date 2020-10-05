from tkinter import Label, Button, Frame, filedialog, simpledialog, messagebox, ttk
from tkinter.ttk import Treeview
from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy
import random
import math


class window(Frame):
    def __init__(self, master=None):
        self.frame = Frame.__init__(self, master)
        self.master = master
        self.initwindow(self.frame)
        # inisiasi frame
    def initwindow(self, master):
        self.master.title("Classification")
        self.master.geometry("1350x670+0+0")  # ukuran size 1350 x 570 posisi awal di 0,0
        self.master.minsize(1350, 670)  # ukuran terkecil (tidak bisa diperkecil lagi)
        self.initmenu(master)
        self.array = []
    def initmenu(self, master):
        self.menubar = Menu(master)
        self.filemenu = Menu(self.menubar, tearoff=0)  # tearoff = menghilangkan garis putus-putus
        self.filemenu.add_command(label="Browse Gambar")
        self.filemenu.add_command(label="Simpan Hasil Proses", state="disable")
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # menambahkan file menu ke menubar


root = Tk()
my_gui = window(root)
root.mainloop()