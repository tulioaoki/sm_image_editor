import cv2

def toEdge(IMAGE_NAME):
    img = cv2.imread(IMAGE_NAME)  # Take the image
    edges = cv2.Canny(img,100,300)    
    cv2.imwrite("./images/PhotoInEdition/edited.jpg", edges)   # Save the image
    return "./images/PhotoInEdition/edited.jpg"