import cv2
import numpy


def toXSobel(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    import numpy
    img = cv2.imread('input.jpg')
    x_sobel = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", x_sobel)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"