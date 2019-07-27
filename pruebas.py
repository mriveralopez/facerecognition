import cv2
import os

def cropFile(pathin, pathout, x, y, w, h):
    img = cv2.imread(pathin)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(pathout, crop_img)

def getImagesPathFromFile(path):
    return os.listdir(path)

imagen_dir = "./people/Screen Shot 2019-07-26 at 15.47.02.png"
cascade_path = "./venv/lib/python3.7/site-packages/cv2/data/"
cascade_dir = cascade_path + "haarcascade_frontalface_alt.xml"

rostroCascade = cv2.CascadeClassifier(cascade_dir)

imagesPath = "./people/"

images = getImagesPathFromFile(imagesPath)
for imagen_dir in images:
    imagen_dir = imagesPath + imagen_dir
    imagen = cv2.imread(imagen_dir)
    filtro = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    rostros = rostroCascade.detectMultiScale(
        filtro,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize= (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    i = 0
    for (x, y, w, h) in rostros:
        dir = imagen_dir.split(".")
        print(dir)

        cropFile(imagen_dir, dir[0] + "." + dir[1] + "_crop" + str(i) + "." + dir[2], x, y, w, h)
        i = i + 1