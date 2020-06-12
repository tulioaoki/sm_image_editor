import cv2
import numpy


def toHighPass(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    import numpy
    img = cv2.imread('input.jpg')
    blur = cv2.GaussianBlur(img,(31,31),0)
    filtered = img - blur
    filtered = filtered + 127*numpy.ones(neg_frame.shape, numpy.uint8)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", filtered)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"