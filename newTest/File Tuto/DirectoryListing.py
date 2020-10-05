import os

listDirectory = os.scandir("C://Users/Sof/Desktop/Master 2/Z-PFE\DataSets/CIFAR100")
for dir in listDirectory:
    print(dir.name)
