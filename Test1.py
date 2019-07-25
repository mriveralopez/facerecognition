import cv2
import face_recognition

new_path = './venv/lib/python3.7/site-packages/cv2/'
faceCascade = cv2.CascadeClassifier(new_path + 'data/haarcascade_frontalface_alt.xml')
#faceCascade = cv2.CascadeClassifier('C:\OpenCV\opencv41\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_alt.xml')

# Load some sample pictures and learn how to recognize them.
image_miguel = face_recognition.load_image_file("people/Miguel Rivera.jpg")
image_encoding_miguel = face_recognition.face_encodings(image_miguel)[0]

image_hugo = face_recognition.load_image_file("people/Navidad.jpg")
image_encoding_hugo = face_recognition.face_encodings(image_hugo)[0]

known_faces = [
    image_encoding_miguel,
    image_encoding_hugo
]

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

    #INICIO JJMD: Reconocimiento Facial
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance = 0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Miguel Rivera"
        elif match[1]:
            name = "Navidad Dulce Navidad"
        else:
            name = "no se quien es"

        face_names.append(name)

        #for (x, y, w, h) in face_locations:
        #    cv2.putText(frame, name, (y, x), font, 0.5, (255, 255, 255), 1)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        #cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 100), font, 0.5, (0, 0, 255), 1)

    #FIN JJMD: Reconocimiento Facial

    if frame is None:
        break

    faces = faceCascade.detectMultiScale(frame)

    # show the frame to our screen
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
    elif key == ord(" "):
        print(name)

# close all windows
cv2.destroyAllWindows()