import cv2


def toNormal(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    cv2.imwrite("../images/edited.jpg", img)   # Save the image
    return "../images/edited.jpg"