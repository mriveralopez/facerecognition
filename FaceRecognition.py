import face_recognition
import cv2

face_locations = []
face_encodings = []
face_names = []
frame_number = 0

vs = cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    print(face_locations)
    for (x, y, w, h) in face_locations:
        cv2.rectangle(rgb_frame, (x, h), (y, w), (255, 0, 0), 2)

    # show the frame to our screen
    cv2.imshow('img', rgb_frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# close all windows
cv2.destroyAllWindows()