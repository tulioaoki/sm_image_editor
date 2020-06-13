from scipy.interpolate import UnivariateSpline
import cv2 
import numpy as np
    

def spreadLookupTable(x, y):
    
    spline = UnivariateSpline(x, y)
    return spline(range(256))


def warm(image,valor):
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, (64+valor), (128+valor), (192+valor), 256] )
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, (64-valor), (128-valor), (192-valor), (256-valor)])

    # Pegar o canal das cores red, green and blue
    red_channel , green_channel, blue_channel = cv2.split(image)

    # Aumentar o canal vermelho e diminuir o azul
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    
    # Juntar de novo os canais (red , green , blue)
    
    return cv2.merge((red_channel, green_channel, blue_channel))


def cold(image,valor):
    
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, (64+valor), (128+valor), (192+valor), 256] )
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, (64-valor), (128-valor), (192-valor), (256-valor)])

    # Pegar o canal das cores red, green and blue
    red_channel, green_channel, blue_channel = cv2.split(image)
    
    # Aumentar o canal azul e diminuir o vermelhor
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    
    # Juntar de novo os canais (red , green , blue)
    
    return cv2.merge((red_channel, green_channel, blue_channel))


def warmth(IMAGE_NAME ,value, imgNumber):

    
    if(value >= 127):

        print("Função Quente")

        multiplicador = value - 127
        result = multiplicador * 0.204
        valor = round(result)
        img  = cv2.imread(IMAGE_NAME)    
        
        
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        print("To salvando em: " + "{}".format(imagem))
        
        final = warm(img,valor) 
        
        cv2.imwrite(imagem , final)   # Save the image
        return "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        

    elif(value < 127):
       
        print("Função fria")
        
        multiplicador = 127 - value

        result = multiplicador * 0.204

        valor = round(result)

        img  = cv2.imread(IMAGE_NAME)    
        
        final = cold(img,valor)

        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        
        cv2.imwrite(imagem , final)   # Save the image
        
        return "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")


