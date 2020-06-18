import cv2


def brilho(IMAGE_NAME, value,imgNumber):
    
    if(value < 128):
        value = 128 - value
    elif(value > 128):
        value = value - 128
    else:
        
        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem

    image = cv2.imread(IMAGE_NAME)
    
    new_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    
    imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

    cv2.imwrite( imagem, new_image)   # Save the image
        
    return imagem
