import cv2
import face_recognition
import os
import time

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
    print(getTime("/", ":") + " loading know faces")
    knowFaces.clear()
    nameFaces.clear()
    imgs = getImagesPathFromFile(path)
    # print(imgs)
    for img in imgs:
        image = face_recognition.load_image_file(path + img)
        image_encoding = face_recognition.face_encodings(image)[0]
        name = img.split(".")[0]
        knowFaces.append(image_encoding)
        nameFaces.append(name)
    print(getTime("/", ":") + " know faces loaded")

def recogniting(knowFaces):
    f = 0

def marcar(face_name, image, status):
    # print(face_name)
    file_name = face_name + " " + getTime("-", "-") + " " + status
    print(file_name)
    cv2.imwrite('./rec/' + file_name + '.jpg', image)

def getTime(dateSplit, timeSplit):
    # return time.strftime("%d" + dateSplit + "%m" + dateSplit + "%y %H" + timeSplit + "%M" + timeSplit + "%S")
    return time.strftime("%y" + dateSplit + "%m" + dateSplit + "%d %H" + timeSplit + "%M" + timeSplit + "%S")

def images():
    imagesPath = "./people/"

    images = getImagesPathFromFile(imagesPath)
    # print(images)
    for imagen_dir in images:
        imagen_dir = imagesPath + imagen_dir
        print(imagen_dir)
        imagen = cv2.imread(imagen_dir)
        filtro = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        rostros = faceCascade.detectMultiScale(
            filtro,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize= (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        # saveFacesWithRectangle(imagen, rostros, imagen_dir, (255, 0, 0), 2)
        saveOnlyFaces(imagen_dir, imagen, rostros)

    cv2.destroyAllWindows()

def video():
    cap = cv2.VideoCapture(0)

    knowFacesPath = "./knowFaces/"

    knowFaces = []
    nameFaces = []

    loadKnowFaces(knowFacesPath, knowFaces, nameFaces)
    r=0

    liveFaces = []
    previousFaces = []

    while True:
        # grab the current frame

        ret, frame = cap.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []

        print(getTime("/", ":") + " frame")
        print(previousFaces)
        print(liveFaces)

        previousFaces = liveFaces
        liveFaces = []

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(knowFaces, face_encoding, tolerance=0.50)
            # print(match.index(True))

            try:
                i = match.index(True)
                face_names.append(nameFaces[i])
                if liveFaces.__contains__(nameFaces[i]):
                    continue
                else:
                    liveFaces.append(nameFaces[i])
            except Exception:
                face_names.append('Desconocido')

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            # cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 5,  bottom - 5), font, 0.5, (255, 255, 0), 1)
            # if(name == "Desconocido"):
            #     name = "Desconocido" + str(knowFaces.__len__())
            #     cropLiveImage(name, frame, top, right, bottom, left)
            #     r = 1

        cv2.imshow("Video", frame)

        # for prev in previousFaces:
        #     if(liveFaces.__contains__(prev)):
        #         continue
        #     else:
        #         marcar(prev, frame, "Entrada")
        #         print(previousFaces)
        #         print(liveFaces)

        for live in liveFaces:
            if (previousFaces.__contains__(live)):
                continue
            else:
                marcar(live, frame, "Entrada")
                print(previousFaces)
                print(liveFaces)

        key = cv2.waitKey(1) & 0xFF

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break
        elif key == ord("r") or r:
            loadKnowFaces(knowFacesPath, knowFaces, nameFaces)
        elif key == ord("h"):
            h = 1
        elif key == ord("e"):
            # print(face_names)
            for face_name in face_names:
                file_name =  face_name + " " + getTime("-", "-") + " Entrada"
                print(file_name)
                cv2.imwrite('./rec/' + file_name + '.jpg', frame)
        elif key == ord("s"):
            # print(face_names)
            for face_name in face_names:
                file_name = face_name + " " + time.strftime("%d-%m-%y %H-%M-%S Salida")
                print(file_name)
                cv2.imwrite('./rec/' + file_name + '.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

print(getTime("/",":") + " init face recognition")
print(getTime("/",":") + " loading cascade path")
cascade_path = "./venv/lib/python3.7/site-packages/cv2/data/"

faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_frontalface_alt.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_profileface.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_eye_tree_eyeglasses.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_eye.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_licence_plate_rus_16stages.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_smile.xml")
# faceCascade = cv2.CascadeClassifier(cascade_path + "haarcascade_fullbody.xml")

print(getTime("/",":") + " cascade path loaded")

video()