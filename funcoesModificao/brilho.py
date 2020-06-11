import cv2


def brilho(IMAGE_NAME, value):
    

    image = cv2.imread(IMAGE_NAME)
    new_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", new_image)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"
