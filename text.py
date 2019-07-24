import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier('/venv/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

img = cv2.imread('vicky.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# if img is None:
#     break

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

emoji = Image.open('emoji.png')

imgPIL = Image.fromarray(gray)

for (x, y, w, h) in faces:
    emoji_resize = emoji.resize((w, h))
    imgPIL.paste(emoji_resize, (x, y), emoji_resize)

imgPIL.save('nueva_imagen.png', "PNG")