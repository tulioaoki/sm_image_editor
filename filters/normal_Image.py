import cv2


def toNormal(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    cv2.imwrite("./images/PhotoInEdition/filtered.jpg", img) 
    return "./images/PhotoInEdition/filtered.jpg"    