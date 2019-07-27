import cv2
import face_recognition
import os
import time

path = './venv/lib/python3.7/site-packages/cv2/'

class Recognition:
    def openWithWebCam(self):
        face_cascade = cv2.CascadeClassifier(path + 'data/haarcascade_frontalface_alt.xml')

        eye_cascade = cv2.CascadeClassifier(path + 'data/haarcascade_eye.xml')

        # smile_cascade = cv2.CascadeClassifier(path + 'data/haarcascade_smile.xml')

        know_faces = []
        name_faces = []
        r = 1

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
                # smiles = smile_cascade.detectMultiScale(roi_gray)
                # for (sx, sy, sw, sh) in smiles:
                #     cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

            cv2.imshow('img', img)

            key = cv2.waitKey(1) & 0xFF

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break

            # if the 'r' key is pressed, reload know faces
            if (key == ord("r") or r):
                r = 0

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
                print("faces loaded")

            # if the spacebar key is pressed, save face
            if key == ord(" "):
                rgb_img = img[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_img)
                face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

                match = []

                for face_encoding in face_encodings:
                    match = face_recognition.compare_faces(know_faces, face_encoding, tolerance = 0.50)

                # print(match)
                i = 0
                while i < match.__len__():
                    if(match[i]):
                        file_name = name_faces[i] + " " + time.strftime("%d-%m-%y %H-%M-%S")
                        print(file_name)
                        cv2.imwrite('./rec/' + file_name + '.jpg', img)
                    i = i + 1

        cap.release()
        cv2.destroyAllWindows()
    def openWithWebCam1(self):
        faceCascade = cv2.CascadeClassifier(path + 'data/haarcascade_frontalface_alt.xml')
        # faceCascade = cv2.CascadeClassifier('C:\OpenCV\opencv41\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_alt.xml')

        known_faces = []
        name_faces = []

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        frame_number = 0

        # grab the reference to the webcam
        vs = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_DUPLEX

        # keep looping
        while True:
            # grab the current frame
            ret, frame = vs.read()

            # INICIO JJMD: Reconocimiento Facial
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

                # If you had more than 2 faces, you could make this logic a lot prettier
                # but I kept it simple for the demo
                i = 0
                name = None
                while i < name_faces.__len__():
                    if match[i]:
                        name = name_faces[i]
                        break
                    i = i + 1

                face_names.append(name)

                # for (x, y, w, h) in face_locations:
                #    cv2.putText(frame, name, (y, x), font, 0.5, (255, 255, 255), 1)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                if not name:
                    continue

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                # cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 100), font, 0.5, (0, 0, 255), 1)

            # FIN JJMD: Reconocimiento Facial

            if frame is None:
                break

            faces = faceCascade.detectMultiScale(frame)

            # show the frame to our screen
            cv2.imshow("Video", frame)
            key = cv2.waitKey(1) & 0xFF

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break
            r=1
            if (key == ord("r") or r):
                r = 0

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
                print("faces loaded")
            elif key == ord(" "):
                print(name)

        # close all windows
        cv2.destroyAllWindows()