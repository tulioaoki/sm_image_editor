import cv2

def rotacionar(IMAGE_NAME ,value):

        if(value < 127):
            value = -(127 - value)
        else:
            value = value - 127
        original=cv2.imread(IMAGE_NAME)
        height, width = original.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), value, 1)
        rotated_image = cv2.warpAffine(original, rotation_matrix, (width, height))
        cv2.imwrite("./images/PhotoInEdition/edited.jpg", rotated_image)   # Save the image
        return "./images/PhotoInEdition/edited.jpg"