import cv2


def smoothTeste(IMAGE_NAME, value):
    if(value%2 == 0): # O valor so pode ser impar
        value += 1

    median = None
    for x in range(3):
        if(x == 0):
            noiseImage = cv2.imread(IMAGE_NAME)  # Take the image
            median = cv2.medianBlur(noiseImage, value)
                    #cv2.GaussianBlur(noiseImage, (value, value), 0)  eh mais suave
        else:
            median = cv2.medianBlur(median, value)
                     #cv2.GaussianBlur(noiseImage, (value, value), 0) eh mais suave
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", median)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"
