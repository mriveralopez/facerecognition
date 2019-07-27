import cv2
from os import scandir

def cropfile(pathin, pathout, x, y, w, h):
    img = cv2.imread(pathin)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(pathout, crop_img)

def ls1(path):
    return [obj.name for obj in scandir(path) if obj.is_file()]

def splitfilename(filename):
    sname = ""
    sext = ""
    i = filename.rfind(".")
    if(i!=0):
        n = len(filename)
        j = n-i-1
        sname = filename[0:i]
        sext = filename[-j:]
    return sext, sname

path = "./people/"
files = ls1(path)
for file in files:
    filea = path + file # archivo original
    sext, sfilename = splitfilename(file)
    filec = path + sfilename + "_crop" + ".png" # archivo crop
    print(filec)
    cropfile(filea, filec, 320, 90, 828, 1100)