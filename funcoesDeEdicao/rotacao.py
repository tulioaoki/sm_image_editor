import cv2

def rotacionar(IMAGE_NAME ,value, imgNumber):

    if(value < 128):
        value = -(128 - value)
    elif(value > 128):
        value = value - 128
    
    else:
        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem
        
    original=cv2.imread(IMAGE_NAME)
    height, width = original.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), value, 1)
    rotated_image = cv2.warpAffine(original, rotation_matrix, (width, height))
    
    imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
    
    cv2.imwrite(imagem , rotated_image)   # Save the image
        
    return "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

    
