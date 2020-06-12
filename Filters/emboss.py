import cv2
import numpy


def toEmboss(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    kernel = numpy.array([[0,-1,-1], [1,0,-1],[1,1,0]])
    embossed = cv2.filter2D(img, -1, kernel)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", embossed)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"