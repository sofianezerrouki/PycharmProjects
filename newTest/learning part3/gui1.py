from tkinter import *
from PIL import ImageTk, Image
import random
import tkinter.simpledialog
import matplotlib.pyplot as plt
import cv2
import numpy as np
import scipy
from scipy import ndimage
from skimage import filters


def show_hist(input_image):

    im = cv2.imread(input_image)
    # calculate mean value from RGB channels and flatten to 1D array
    vals = im.mean(axis=2).flatten()
    # plot histogram with 255 bins
    b, bins, patches = plt.hist(vals, 255)
    plt.xlim([0, 255])
    plt.show()


class MyDialog(tkinter.simpledialog.Dialog):

    def body(self, master):
        Label(master, text="Threshold:").grid(row=0)

        self.e1 = Entry(master)

        self.e1.grid(row=0, column=1)

    def apply(self):
        first = int(self.e1.get())
        self.result = first


def display_image(input_image):
    print("display_image called")
    canvas.delete("pyramid")
    path = input_image
    global img
    img = ImageTk.PhotoImage(Image.open(path))
    canvas.itemconfig(img_on_can, image=img)
    # or i in range(1000000000000):
    # pass
    # print("display_image returning")
    return


def binary(input_image):
    # print(input_image)
    path = input_image
    binary_img = Image.open(path)
    pixel_val = binary_img.load()
    d = MyDialog(root)
    # d.result is the threshold value

    for i in range(binary_img.size[0]):
        for j in range(binary_img.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            if (sum // 3 > d.result):
                pixel_val[i, j] = (255, 255, 255)
            else:
                pixel_val[i, j] = (0, 0, 0)
    # print(d.result)
    # print(pixel_val[0,0][0])
    img_path = "Binary.jpg"
    binary_img.save(img_path)
    display_image(img_path)
    return


def gray_scale(input_image):
    gray_img = Image.open(input_image)
    pixel_val = gray_img.load()
    print(pixel_val[0, 0])
    for i in range(gray_img.size[0]):
        for j in range(gray_img.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            pixel_val[i, j] = (sum // 3, sum // 3, sum // 3)
    img_path = "Gray.jpg"
    gray_img.save(img_path)
    display_image(img_path)

    # img = Image.open(input_image).convert('LA')
    # img.save("Gray.png")
    # display_image("Gray.png")

    return


def corrupt(input_image):
    corrupt_img = Image.open(input_image)
    pixel_val = corrupt_img.load()
    # print(pixel_val[0,0])
    for i in range(corrupt_img.size[0]):
        for j in range(corrupt_img.size[1]):
            if (random.randint(1, 10) < 3):
                # print("Corrupting pixel : "+str(i)+" "+str(j))
                pixel_val[i, j] = (0, 0, 0)
    img_path = "Output.jpg"
    corrupt_img.save(img_path)

    # Edit the pixel values and then save them as a new image
    display_image(img_path)
    return


def binary_it(input_image):
    path = input_image
    binary_it_image = Image.open(path)
    pixel_val = binary_it_image.load()
    temp = pixel_val
    temp1 = pixel_val
    threshold_value = MyDialog(root).result
    margin = 5
    list0 = []
    list1 = []
    b = True
    while (b):
        temp = temp1
        list0[:] = []
        list1[:] = []
        for i in range(binary_it_image.size[0]):
            for j in range(binary_it_image.size[1]):
                sum1 = 0
                for k in range(0, 3):
                    sum1 += pixel_val[i, j][k]
                sum1 = sum1 // 3
                if (sum1 > threshold_value):
                    list0.append(sum1)
                else:
                    list1.append(sum1)

        avg_small = sum(list0) // len(list0)
        avg_big = sum(list1) // len(list1)
        new_threshold = (avg_big + avg_small) // 2
        print(str(new_threshold) + "new threshold value obtained")
        if (abs(new_threshold - threshold_value) < margin):
            b = False
        else:
            threshold_value = new_threshold

        for i in range(binary_it_image.size[0]):
            for j in range(binary_it_image.size[1]):
                sum1 = 0
                for k in range(0, 3):
                    sum1 += temp[i, j][k]
                sum1 = sum1 // 3
                if (sum1 > threshold_value):
                    temp[i, j] = (255, 255, 255)
                else:
                    temp[i, j] = (0, 0, 0)
        pixel_val = temp
        img_path = "BinaryIT.jpg"
        binary_it_image.save(img_path)
        display_image(img_path)
    return


def first_Order1(image_path):
    image = cv2.imread(image_path)
    new_path = "First_Order.jpg"
    highRes = cv2.pyrUp(image)
    cv2.imwrite(new_path, highRes)
    display_image(new_path)
    return


def binary_pt(input_image):
    hist = []
    for i in range(0, 377):
        hist.append(0)
    binary_pt_image = Image.open(input_image)
    pixel_val = binary_pt_image.load()

    for i in range(binary_pt_image.size[0]):
        for j in range(binary_pt_image.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            sum = sum // 3
            # print(sum)
            hist[sum] += 1
    percentage = 30
    threshold_pixels = binary_pt_image.size[0] * binary_pt_image.size[1] * 0.6
    print(binary_pt_image.size[0] * binary_pt_image.size[1])
    print(threshold_pixels)

    for i in range(376, -1, -1):

        sum += hist[i]
        if (sum > threshold_pixels):
            threshold_value = i
            break
    print(threshold_value)
    for i in range(binary_pt_image.size[0]):
        for j in range(binary_pt_image.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            sum = sum // 3
            if (sum > threshold_value):
                pixel_val[i, j] = (255, 255, 255)
            else:
                pixel_val[i, j] = (0, 0, 0)

    img_path = "BinaryPT.jpg"
    binary_pt_image.save(img_path)

    # Edit the pixel values and then save them as a new image
    display_image(img_path)
    return


def reduce_noise(input_image):
    noises_image = Image.open("Output.jpg")
    pixel_val = noises_image.load()
    temp = pixel_val
    temp1 = pixel_val
    for i in range(2, noises_image.size[0] - 2):
        for j in range(2, noises_image.size[1] - 2):
            # sum0=sum1=sum2=0
            # for k in range(i-2,i+3):
            #	for l in range(j-2,j+3):
            #			sum0 += temp[k,l][0]
            #			sum1 += temp[k,l][1]
            #			sum2 += temp[k,l][2]

            #	temp1[i,j] = (sum0//25,sum1//25,sum2//25)
            sum0 = (temp[i, j][0] + temp[i - 1, j][0] + temp[i + 1, j][0] + temp[i, j + 1][0] + temp[i, j - 1][0]) // 5
            sum1 = (temp[i, j][1] + temp[i - 1, j][1] + temp[i + 1, j][1] + temp[i, j + 1][1] + temp[i, j - 1][1]) // 5
            sum2 = (temp[i, j][2] + temp[i - 1, j][2] + temp[i + 1, j][2] + temp[i, j + 1][2] + temp[i, j - 1][2]) // 5
            temp1[i, j] = (sum0, sum1, sum2)

    pixel_val = temp1
    print("Noise Reduced")
    img_path = "NoiseSimple.jpg"
    noises_image.save(img_path)
    display_image(img_path)
    return


def reduce_noise_mf(input_image):
    noises_image = Image.open("Output.jpg")
    pixel_val = noises_image.load()

    list0 = []
    list1 = []
    list2 = []
    temp = pixel_val
    temp1 = pixel_val
    for i in range(1, noises_image.size[0] - 1):

        for j in range(1, noises_image.size[1] - 1):
            list0.append(temp[i, j][0])
            list0.append(temp[i - 1, j][0])
            list0.append(temp[i + 1, j][0])
            list0.append(temp[i, j - 1][0])
            list0.append(temp[i, j + 1][0])
            list0.append(temp[i - 1, j - 1][0])
            list0.append(temp[i + 1, j - 1][0])
            list0.append(temp[i - 1, j + 1][0])
            list0.append(temp[i + 1, j + 1][0])
            # print(str(list0)+"\n")
            list1.append(temp[i, j][1])
            list1.append(temp[i - 1, j][1])
            list1.append(temp[i + 1, j][1])
            list1.append(temp[i, j - 1][1])
            list1.append(temp[i, j + 1][1])
            list1.append(temp[i - 1, j - 1][1])
            list1.append(temp[i + 1, j - 1][1])
            list1.append(temp[i - 1, j + 1][1])
            list1.append(temp[i + 1, j + 1][1])
            # print(list1)
            list2.append(temp[i, j][2])
            list2.append(temp[i - 1, j][2])
            list2.append(temp[i + 1, j][2])
            list2.append(temp[i, j - 1][2])
            list2.append(temp[i, j + 1][2])
            list2.append(temp[i - 1, j - 1][2])
            list2.append(temp[i + 1, j - 1][2])
            list2.append(temp[i - 1, j + 1][2])
            list2.append(temp[i + 1, j + 1][2])
            # print(list2)
            list0.sort()
            list1.sort()
            list2.sort()
            temp1[i, j] = (list0[4], list1[4], list2[4])
            list0[:] = []
            list1[:] = []
            list2[:] = []

    pixel_val = temp1
    print("Noise Reduced")
    img_path = "NoiseMedian.jpg"
    noises_image.save(img_path)
    display_image(img_path)
    return


def label_bw(input_image):  # This function is copied from the internet
    img = cv2.imread(input_image, 0)
    img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)[1]  # ensure binary
    ret, labels = cv2.connectedComponents(img)

    # Map component labels to hue val
    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_BGR2GRAY)

    # set bg label to black
    labeled_img[label_hue == 0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()
    return


# print(new_list)


def my_roberts(image_path):
    roberts_image = cv2.imread(image_path, 0)
    temp = roberts_image.copy()

    for i in range(0, roberts_image.shape[0] - 1):
        for j in range(0, roberts_image.shape[1] - 1):
            A = abs(roberts_image.item(i, j) - roberts_image.item(i + 1, j + 1))
            B = abs(roberts_image.item(i + 1, j) - roberts_image.item(i, j + 1))
            temp.itemset((i, j), max(A, B))
    img_path = "Roberts.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    return


def my_sobel(image_path):
    # display_image(image_path)

    im = scipy.misc.imread(image_path)
    im = im.astype('int32')
    dx = ndimage.sobel(im, 0)  # horizontal derivative
    dy = ndimage.sobel(im, 1)  # vertical derivative
    mag = np.hypot(dx, dy)  # magnitude
    mag *= 255.0 / np.max(mag)  # normalize (Q&D)
    scipy.misc.imsave('sobel.jpg', mag)
    display_image('sobel.jpg')

    return


def my_prewitt(image_path):
    im = cv2.imread(image_path, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0] - 1):
        for j in range(1, im.shape[1] - 1):
            A = abs(im.item(i - 1, j - 1) + im.item(i - 1, j) + im.item(i - 1, j + 1) - im.item(i + 1, j + 1) - im.item(
                i + 1, j) - im.item(i + 1, j - 1))
            B = abs(im.item(i - 1, j + 1) + im.item(i, j + 1) + im.item(i + 1, j + 1) - im.item(i + 1, j - 1) - im.item(
                i - 1, j + 1) - im.item(i, j + 1))
            mag = (A * A + B * B) ** (.5)
            temp.itemset((i, j), mag)
    img_path = "Prewitt.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    # im = scipy.misc.imread(image_path)
    # im = im.astype('int32')
    # dx = ndimage.prewitt(im, 0)  # horizontal derivative
    # dy = ndimage.prewitt(im, 1)  # vertical derivative
    # mag = np.hypot(dx, dy)  # magnitude
    # mag *= 255.0 / np.max(mag)  # normalize (Q&D)
    # scipy.misc.imsave('prewitt.jpg', mag)
    # display_image('prewitt.jpg')
    return


def my_kirsh(image_path):
    im = cv2.imread(image_path, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0] - 1):
        for j in range(1, im.shape[1] - 1):
            A = abs(
                im.item(i - 1, j) + im.item(i, j + 1) + im.item(i + 1, j - 1) - im.item(i + 1, j - 1) - im.item(i + 1,
                                                                                                                j) - im.item(
                    i, j - 1))
            B = abs(im.item(i - 1, j - 1) + im.item(i, j - 1) + im.item(i - 1, j) - im.item(i + 1, j + 1) - im.item(i,
                                                                                                                    j + 1) - im.item(
                i + 1, j))
            mag = (A * A + B * B) ** (.5)
            temp.itemset((i, j), mag)

    img_path = "Kirsh.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)


def my_laplacian(image_path):
    im = cv2.imread(image_path, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0] - 1):
        for j in range(1, im.shape[1] - 1):
            A = (4 * im.item(i, j) - im.item(i, j + 1) - im.item(i + 1, j) - im.item(i - 1, j) - im.item(i, j - 1))
            # B = abs(im.item(i-1,j-1)+im.item(i,j-1)+im.item(i-1,j)-im.item(i+1,j+1)-im.item(i,j+1)-im.item(i+1,j))
            # mag = (A*A + B*B)**(.5)
            if (A < 0):
                temp.itemset((i, j), 0)
            elif (A > 255):
                temp.itemset((i, j), 255)
            else:
                temp.itemset((i, j), A)

    img_path = "Laplacian.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    return


def my_full_laplacian(image_path):
    im = cv2.imread(image_path, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0] - 1):
        for j in range(1, im.shape[1] - 1):
            A = abs(-8 * im.item(i, j) + im.item(i, j + 1) + im.item(i + 1, j) + im.item(i - 1, j) + im.item(i,
                                                                                                             j - 1) + im.item(
                i - 1, j + 1) + im.item(i + 1, j + 1) + im.item(i - 1, j - 1) + im.item(i + 1, j - 1))
            # B = abs(im.item(i-1,j-1)+im.item(i,j-1)+im.item(i-1,j)-im.item(i+1,j+1)-im.item(i,j+1)-im.item(i+1,j))
            # mag = (A*A + B*B)**(.5)
            if (A < 0):
                temp.itemset((i, j), 0)
            else:
                temp.itemset((i, j), A)

    img_path = "Laplacian_81.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    return


def display_image_pyr(input_image):
    # print("display_image called")
    photo = input_image
    width = 0
    i = 0
    global im_pyr
    length = [430, 635, 740, 795, 825, 840]
    im_pyr = []
    for p in photo:
        im_pyr.append(ImageTk.PhotoImage(Image.open(p)))
        s = Image.open(p)

        # sizes = im.load()
        width += s.size[0]
        # length.append(width)
        # print(i)

        i += 1

    canvas.itemconfig(img_on_can, image=im_pyr[0])
    for i in range(0, 5):
        print(length[i])
        canvas.create_image(length[i + 1], 20, anchor=NE, image=im_pyr[i + 1], tags="pyramid")

    # img_on_can = canvas.create_image(20, w, image=img_pyr)
    # canvas.image = img_pyr
    # or i in range(1000000000000):
    # pass
    # print("display_image returning")
    return


def my_pyramid(image_path):
    i = 0
    total_width = 0
    # photos = []
    A = ["LowerPyramid0.jpg", "LowerPyramid1.jpg", "LowerPyramid2.jpg", "LowerPyramid3.jpg", "LowerPyramid4.jpg"]
    while (i < 6):
        # print("Iteration no : "+str(i))
        im = cv2.imread(image_path)

        # print("Old"+image_path)
        img_path = "LowerPyramid" + str(i) + ".jpg"
        lowerRes = cv2.pyrDown(im)
        cv2.imwrite(img_path, lowerRes)
        total_width += lowerRes.shape[1]
        image_path = img_path
        # print("width"+str(total_width))
        # print("New "+image_path)
        # print(im.shape[1]//2)
        i += 1
    display_image_pyr(A)
    return


def trying_pyramid(image_path):
    k = 0
    A = ["LowerPyramid0.jpg", "LowerPyramid1.jpg", "LowerPyramid2.jpg", "LowerPyramid3.jpg", "LowerPyramid4.jpg",
         "LowerPyramid5.jpg"]
    while (k < 6):
        im = cv2.imread(image_path, 0)
        temp = np.ndarray(shape=(im.shape[0] // 2, im.shape[1] // 2))
        for i in range(1, im.shape[0] - 1, 1):
            for j in range(1, im.shape[1] - 1, 1):
                # if(im.item(i+1,j+1)):
                # print(str(i)+" "+str(j))
                # print(im.item(i,j))
                # avg1 = (im.item(i,j,0)+im.item(i+1,j,0)+im.item(i+1,j-1,0)+im.item(i,j-1,0))//4
                # avg2 = (im.item(i,j,1)+im.item(i+1,j,1)+im.item(i+1,j-1,1)+im.item(i,j-1,1))//4
                # avg3 = (im.item(i,j,2)+im.item(i+1,j,2)+im.item(i+1,j-1,2)+im.item(i,j-1,2))//4

                avg = (im.item(i, j) + im.item(i + 1, j) + im.item(i + 1, j - 1) + im.item(i, j - 1)) // 4
                temp.itemset((i // 2, j // 2), avg)
        img_path = A[k]
        cv2.imwrite(img_path, temp)
        image_path = A[k]
        # display_image(img_path)
        k += 1
    display_image_pyr(A)
    return


def zero_Order(image_path):
    im = cv2.imread(image_path, 0)
    temp = np.ndarray(shape=(im.shape[0] * 2, im.shape[1] * 2))

    for i in range(0, im.shape[0]):
        for j in range(0, im.shape[1]):
            temp.itemset((i * 2, j * 2), im.item(i, j))
            temp.itemset((i * 2 + 1, j * 2), im.item(i, j))
            temp.itemset((i * 2, j * 2 + 1), im.item(i, j))
            temp.itemset((i * 2 + 1, j * 2 + 1), im.item(i, j))
    print(im.item(1, 1))
    img_path = "Zero.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    return


def first_Order(image_path):
    im = cv2.imread(image_path, 0)
    temp = np.ndarray(shape=((im.shape[0] * 2) + 1, (im.shape[1] * 2) + 1))

    for i in range(0, im.shape[0] * 2 + 1):
        for j in range(0, im.shape[1] * 2 + 1):
            if ((i % 2 == 0) or (j % 2 == 0)):
                temp.itemset((i, j), int(0))
            else:
                temp.itemset((i, j), int(im.item((i - 1) // 2, (j - 1) // 2)))
            # print(im.item((i-1)//2,(j-1)//2))
    print(temp.item(1, 1))
    temp1 = temp
    # print(temp1)
    # counti = 1
    # countj = 1
    # print(temp1.item(0,0)//2)
    new_value = 0
    for i in range(1, im.shape[0] * 2):
        # countj = 1
        for j in range(1, im.shape[1] * 2):

            new_value = ((temp1.item(i - 1, j) // 2) + (temp1.item(i + 1, j) // 2) + (temp1.item(i, j - 1) // 2) + (
                        temp1.item(i, j + 1) // 2) + (temp1.item(i - 1, j - 1) // 4) + (
                                     temp1.item(i - 1, j + 1) // 4) + (temp1.item(i + 1, j - 1) // 4) + (
                                     temp1.item(i + 1, j + 1) // 4) + (temp1.item(i, j)))
            if (i < 10 and j < 10):
                print(temp1.item(i - 1, j))
            # print(new_value)
            temp.itemset((i, j), new_value)

        # if(countj>im.shape[1]-2):
        #	break
        # countj += 2
    # if(counti>im.shape[0]*2-2):
    #	break
    # counti += 2
    img_path = "First_Order.jpg"
    cv2.imwrite(img_path, temp)
    display_image(img_path)
    return


root = Tk()
image_path = "newyork.jpg"
gray_image_path = "Gray.jpg"
canvas = Canvas(root, width=1000, height=700)
canvas.pack()
test_image = ImageTk.PhotoImage(Image.open(image_path))
img_on_can = canvas.create_image(20, 20, anchor=NW, image=test_image)
canvas.image = test_image
im = cv2.imread(image_path)
# print(im[1,1])

button = Button(root, text="Corrupt", command=lambda: corrupt(image_path))
button = canvas.create_window(10, 630, anchor=NW, window=button)

button = Button(root, text="Reduce Noise (S)", command=lambda: reduce_noise(image_path))
button = canvas.create_window(85, 630, anchor=NW, window=button)

button = Button(root, text="Reduce Noise (MF)", command=lambda: reduce_noise_mf(image_path))
button = canvas.create_window(210, 630, anchor=NW, window=button)

button = Button(root, text="Binary (T)", command=lambda: binary(image_path))
button = canvas.create_window(350, 630, anchor=NW, window=button)

button = Button(root, text="Binary (PT)", command=lambda: binary_pt(image_path))
button = canvas.create_window(430, 630, anchor=NW, window=button)

button = Button(root, text="Binary (IT)", command=lambda: binary_it(image_path))
button = canvas.create_window(530, 630, anchor=NW, window=button)

button = Button(root, text="Label BW", command=lambda: label_bw(image_path))
button = canvas.create_window(630, 630, anchor=NW, window=button)

button = Button(root, text="Gray Scale", command=lambda: gray_scale(image_path))
button = canvas.create_window(730, 630, anchor=NW, window=button)

button = Button(root, text="Histogram", command=lambda: show_hist(image_path))
button = canvas.create_window(830, 630, anchor=NW, window=button)

button = Button(root, text="Robert's", command=lambda: my_roberts(gray_image_path))
button = canvas.create_window(10, 570, anchor=NW, window=button)

button = Button(root, text="Sobel", command=lambda: my_sobel(gray_image_path))
button = canvas.create_window(85, 570, anchor=NW, window=button)

button = Button(root, text="Prewitt", command=lambda: my_prewitt(gray_image_path))
button = canvas.create_window(210, 570, anchor=NW, window=button)

button = Button(root, text="Kirsh", command=lambda: my_kirsh(gray_image_path))
button = canvas.create_window(350, 570, anchor=NW, window=button)

button = Button(root, text="Laplacian", command=lambda: my_laplacian(gray_image_path))
button = canvas.create_window(430, 570, anchor=NW, window=button)

button = Button(root, text="Laplacian(-8,1)", command=lambda: my_full_laplacian(gray_image_path))
button = canvas.create_window(530, 570, anchor=NW, window=button)

button = Button(root, text="Pyramid", command=lambda: trying_pyramid(image_path))
button = canvas.create_window(630, 570, anchor=NW, window=button)

button = Button(root, text="Zero Order", command=lambda: zero_Order("LowerPyramid0.jpg"))
button = canvas.create_window(730, 570, anchor=NW, window=button)

button = Button(root, text="First Order", command=lambda: first_Order1("LowerPyramid0.jpg"))
button = canvas.create_window(830, 570, anchor=NW, window=button)

root.mainloop()