import cv2
import opencv as cv

def images(faceCascade):
    imagesPath = "./people/"

    images = cv.getImagesPathFromFile(imagesPath)
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

        cv.saveFacesWithRectangle(imagen, rostros, imagen_dir, (255, 0, 0), 2)
        # cv.saveOnlyFaces(imagen_dir, imagen, rostros)

    cv2.destroyAllWindows()