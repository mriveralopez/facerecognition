import cv2
import Utils as util

def marcar(face_name, image, status):
    file_name = face_name + " " + util.getTime("-", "-") + " " + status
    print(file_name)
    cv2.imwrite('./rec/' + file_name + '.jpg', image)