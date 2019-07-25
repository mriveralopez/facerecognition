import cv2
import face_recognition
import numpy as np
import os

path = './venv/lib/python3.7/site-packages/cv2/'

class Recognition:
    def openWithWebCam(self):
        face_cascade = cv2.CascadeClassifier(path + 'data/haarcascade_frontalface_alt.xml')

        eye_cascade = cv2.CascadeClassifier(path + 'data/haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('img', img)

            key = cv2.waitKey(1) & 0xFF

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break
            # if the spacebar key is pressed, save face
            if key == ord(" "):
                directory = "./people/"

                know_faces = []
                name_faces = []

                for file in os.listdir(directory):
                    # print(os.path.join(directory, file))
                    name = file.split(".")[0]
                    # print(name)
                    image = face_recognition.load_image_file(os.path.join(directory, file))
                    image_encoding = face_recognition.face_encodings(image)[0]
                    know_faces.append(image_encoding)
                    name_faces.append(name)

                rgb_img = img[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_img)
                face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

                for face_encoding in face_encodings:
                    match = face_recognition.compare_faces(know_faces, face_encoding, tolerance=0.50)
                    print(match)

        cap.release()
        cv2.destroyAllWindows()

    def readFacesFromPicturesFiles(self, img):
        import os
        import face_recognition

        directory = "./people/"

        know_faces = []
        name_faces = []

        for file in os.listdir(directory):
            # print(os.path.join(directory, file))
            name = file.split(".")[0]
            # print(name)
            image = face_recognition.load_image_file(file)
            image_encoding = face_recognition.face_encodings(image)[0]
            know_faces.append(image_encoding)
            name_faces.append(name)

        Recognition.writeNames(img, know_faces, name_faces)

    def writeNames(self, img, know_faces, names_faces):
        import face_recognition
        
        rgb_img = img[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(know_faces, face_encoding, tolerance=0.50)
            print(match)