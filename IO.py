import cv2
import Utils as util
import WS

def marcar(face_name, image, status):
    file_name = face_name + " " + util.getTime("-", "-") + " " + status
    print(file_name)
    data = {'code' : face_name, 'status' : status}
    WS.POST('Assistance/add.php', data)
    # WS.GET('Assistance/add.php?code=' + face_name + '&status=' + status)
    cv2.imwrite('./rec/' + file_name + '.jpg', image)