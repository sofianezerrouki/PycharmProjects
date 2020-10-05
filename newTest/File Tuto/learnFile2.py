import shutil
import os

source = "2.jpg"
target = "images/2.jpg"

shutil.copy(source,target) #shutil => pour copier couper ,supprimer des fichier ...
os.remove(source)