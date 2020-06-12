import cv2


def toGray(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # To gray
    cv2.imwrite("./images/PhotoInEdition/filtered.jpg", gray)   # Save the image
    return "./images/PhotoInEdition/filtered.jpg"