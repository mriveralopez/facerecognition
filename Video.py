import cv2
import IO as io
import opencv as cv
import Utils as util

def video():

    print(util.getTime("/", ":") + " loading Video Capture")

    cap = []
    cap.append(cv2.VideoCapture(0))
    # cap.append(cv2.VideoCapture(0))

    print(util.getTime("/", ":") + " Video Capture loaded")

    knowFacesPath = "./knowFaces/"

    knowFaces = []
    nameFaces = []

    cv.loadKnowFacesFromDB(knowFacesPath, knowFaces, nameFaces)
    r = 0

    liveFaces = []
    previousFaces = []

    while True:
        fr = []
        for cam in cap:
            # grab the current frame

            ret, frame = cam.read()

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame of video
            face_locations = cv.face_recognition.face_locations(rgb_frame)
            face_encodings = cv.face_recognition.face_encodings(rgb_frame, face_locations)

            face_names = []

            print(util.getTime("/", ":") + " frame")
            print(previousFaces)
            print(liveFaces)

            previousFaces = liveFaces
            liveFaces = []

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = cv.face_recognition.compare_faces(knowFaces, face_encoding, tolerance=0.50)
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

            # cv2.imshow("Video", frame)
            fr.append(frame)

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
                    io.marcar(live, frame, "dos camaras")
                    print(previousFaces)
                    print(liveFaces)

            key = cv2.waitKey(1) & 0xFF

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break
            elif key == ord("r") or r:
                cv.loadKnowFacesFromDB(knowFacesPath, knowFaces, nameFaces)
            elif key == ord("h"):
                h = 1
            elif key == ord("e"):
                # print(face_names)
                for face_name in face_names:
                    file_name =  face_name + " " + util.getTime("-", "-") + " Entrada"
                    print(file_name)
                    cv2.imwrite('./rec/' + file_name + '.jpg', frame)
            elif key == ord("s"):
                # print(face_names)
                for face_name in face_names:
                    file_name = face_name + " " + util.getTime("-", "-") + " Salida"
                    print(file_name)
                    cv2.imwrite('./rec/' + file_name + '.jpg', frame)

        cv2.imshow("frame", frame)
        # cv2.imshow("camara 1", fr[0])
        # cv2.imshow("camara 2", fr[1])
    cv2.destroyAllWindows()