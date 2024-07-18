from email.mime import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('asset/image.png')
plt.imshow(image)
plt.show