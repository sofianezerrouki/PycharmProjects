import matplotlib.pyplot as plt

#load data from image
data  = plt.imread("../home work/5.png")

#show image
plt.imshow(data)
plt.show()

# Set the red channel in this part of the image to 1
data[:100, :10, 0] = 1

# Set the green channel in this part of the image to 0
data[:10, :100, 1] = 0

# Set the blue channel in this part of the image to 0
data[:100, :10, 2] = 0

# Visualize the result
plt.imshow(data)
plt.show()