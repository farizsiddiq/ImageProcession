from email.mime import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('asset/test.png')
plt.imshow(image)
plt.show()