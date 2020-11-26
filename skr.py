import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL
import os
import glob



exit()


im = Image.open("bliss.jpg")

im.save("compressed_bliss_10.jpg", quality=10)
im.save("compressed_bliss_30.jpg", quality=30)
im.save("compressed_bliss_50.jpg", quality=50)
im.save("compressed_bliss_70.jpg", quality=70)
im.save("compressed_bliss_90.jpg", quality=90)

np.noisy

exit(0)

img = plt.imread('bliss.jpg')

print(img.dtype)
print(img.shape)

plt.subplot(2,3,1)
plt.imshow(img)

R=img[:,:,0]
plt.subplot(2,3,2)
plt.imshow(R)

plt.subplot(2,3,3)
plt.imshow(R, cmap=plt.cm.gray)

R_better_one = np.dot(img[...,:3], [0.2990, 0.5870, 0.1440])
R_better_two = np.dot(img[...,:3], [0.2126, 0.7152, 0.0722])

plt.subplot(2,3,4)
plt.imshow(R_better_one, cmap=plt.cm.gray)

plt.subplot(2,3,5)
plt.imshow(R_better_two, cmap=plt.cm.gray)

plt.show()