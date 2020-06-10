import cv2


def smooth(IMAGE_NAME):
    median = None
    for x in range(3):
        if(x == 0):
            noiseImage = cv2.imread(IMAGE_NAME)  # Take the image
            median = cv2.medianBlur(noiseImage, 7)
        else:
            median = cv2.medianBlur(median, 7)

    cv2.imwrite("./images/PhotoInEdition/edited.jpg", median)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"
