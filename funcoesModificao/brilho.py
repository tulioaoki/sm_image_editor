import cv2


def brilho(IMAGE_NAME, value,imgNumber):
    
    if(value < 127):
        value = -(127 - value)
    else:
        value = value - 127
        
    image = cv2.imread(IMAGE_NAME)
    new_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    
    imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

    cv2.imwrite( imagem, new_image)   # Save the image
        
    return imagem
