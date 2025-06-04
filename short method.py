from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha(width=300, height=100)
captcha_text = input("Enter CAPTCHA text: ")
filename = 'CAPTCHA1.png'
image.write(captcha_text, filename)
img = Image.open(filename)
img.show()