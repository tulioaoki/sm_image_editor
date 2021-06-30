# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

def luminancia (IMAGE_NAME, value, imgNumber): # [Value eh o valor do gamma]
    # [Calcula o valor equivalente do value]
    
    if(value == 128):
        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem
    else:

        multiplicador = 255 -(255 - value)
        result = multiplicador * 0.015748031   #  0.015748031= 2/127    2:limite  127: possibilidades
        value = result
        if(value == 0):
            value = 0.015748031
            
        # [Le imagem]
        img = cv2.imread(IMAGE_NAME)

        # [Aplica valor de gamma (value)]
        invGamma = 1.0 / value
        table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")
        newImage = cv2.LUT(img, table)

        # [Salva o caminho da imagem]
        imagePath = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

        # [Salva a imagem]
        cv2.imwrite(imagePath, newImage) 
        return imagePath