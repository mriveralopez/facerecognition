import cv2
import face_recognition
import os
import Utils as util
import WS
from pprint import pprint

def getImagesPathFromFile(path):
    images = []
    for file in os.listdir(path):
        name = file.split(".")
        if(name[1] == "jpg" or name[1] == "jpeg" or name[1] == "png"):
            images.append(name[0] + "." + name[1])
    return images

def cropFile(pathin, pathout, x, y, w, h):
    img = cv2.imread(pathin)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(pathout, crop_img)

def cropLiveImage(name, frame, x, y, w, h):
    crop_img = frame[y:y+h, x:x+w]
    cv2.imwrite('./knowFaces/' + name + '.jpg', crop_img)

def saveOnlyFaces(imagen_dir, img, faces):
    i = 0
    for (x, y, w, h) in faces:
        dir = imagen_dir.split(".")
        dir = dir[0] + "." + dir[1] + "_crop" + str(i) + "." + dir[2]
        # print(dir)
        cropFile(imagen_dir, dir, x, y, w, h)
        i = i + 1

def drawRectangle(imagen, x, y, w, h, color, width):
    cv2.rectangle(imagen, (x, y), (x + w, y + h), color, width)

def saveFacesWithRectangle(img, faces, imagen_dir, color, width):
    for (x, y, w, h) in faces:
        dir = imagen_dir.split(".")
        dir = dir[0] + "." + dir[1] + "_rectangle." + dir[2]
        print(dir)
        drawRectangle(img, x, y, w, h, color, width)
    cv2.imwrite(dir, img)

def loadKnowFaces(path, knowFaces, nameFaces):
    print(util.getTime("/", ":") + " loading know faces")
    knowFaces.clear()
    nameFaces.clear()
    imgs = getImagesPathFromFile(path)
    for img in imgs:
        image = face_recognition.load_image_file(path + img)
        image_encoding = face_recognition.face_encodings(image)[0]
        name = img.split(".")[0]
        knowFaces.append(image_encoding)
        nameFaces.append(name)
    print(util.getTime("/", ":") + " know faces loaded")

def loadKnowFacesFromDB(path, knowFaces, nameFaces):
    print(util.getTime("/", ":") + " loading know faces from DB")

    knowFaces.clear()
    nameFaces.clear()

    employees = WS.GET("Employee/list.php")

    print(employees)

    for employee in employees.json():
        image = face_recognition.load_image_file(path + employee.get('code') + ".png")
        image_encoding = face_recognition.face_encodings(image)[0]
        name = employee.get('code')
        knowFaces.append(image_encoding)
        nameFaces.append(name)
    print(util.getTime("/", ":") + " know faces loaded from DB")

# def recogniting(knowFaces):
#     f = 0