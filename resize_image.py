# Improting Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"test_image.jpg")

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size

print(width, height)

newsize = (1500, 800)
im1 = im.resize(newsize)
# Shows the image in image viewer
im1.show()
im1.save('test_resize.jpeg', 'JPEG')