import cv2
import numpy


def toLaplacian(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    import numpy
    img = cv2.imread('input.jpg')
    lapl = cv2.Laplacian(img,cv2.CV_64F, ksize=5)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", filtered)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"