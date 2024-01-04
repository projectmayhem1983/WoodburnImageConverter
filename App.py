import os
import cv2
import matplotlib.pyplot as plt

counter = 0
filename = "converted{}.png"
while os.path.isfile(filename.format(counter)):
    counter += 1
filename = filename.format(counter)
image_to_convert = input("Please type file name to convert. Extension must be lowercase.")
image = cv2.imread(image_to_convert)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 5, 50)
edges_inv = cv2.bitwise_not(edges)
plt.imshow(edges_inv, cmap='gray')
cv2.imwrite(filename, edges_inv)
