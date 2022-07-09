import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./bmp/Lenna.bmp')
plt.imshow(img)

plt.show()