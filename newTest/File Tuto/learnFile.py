students_list = ["Yassine","hakim","karim","ABD RAHIM","Sofiane"]

with open("file1.txt","w+") as file :
    for student in students_list:
        file .write(student+"\n")
    file.close()
