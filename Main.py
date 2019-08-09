import cv2
import Images as images
import Utils as util
import Video as video

print(util.getTime("/", ":") + " init face recognition")
print(util.getTime("/", ":") + " loading cascade path")
cascade_path = "./venv/lib/python3.7/site-packages/cv2/data/"

faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_frontalface_alt.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_profileface.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_eye_tree_eyeglasses.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_eye.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_licence_plate_rus_16stages.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_smile.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_fullbody.xml")

print(util.getTime("/", ":") + " cascade path loaded")

video.video()
# images.images(faceCascade)