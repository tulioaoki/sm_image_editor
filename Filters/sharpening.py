import cv2


def toSharp(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpned = cv2.filter2D(img, -1, kernel)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", sharpned)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"