import os
import random

if os.path.exists("file1.txt"):

    with open("file1.txt","r+") as file :
        #print(file.readlines()) # controle + click sur readlines()
        fileList = file.readlines()
        fileChoise = random.choice(fileList)
        print("Le cadeau : "+fileChoise)
        file.close()
else :
    print("le document n'exist pas ! attention ")