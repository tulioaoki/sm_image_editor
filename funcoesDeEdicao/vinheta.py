import cv2
import numpy as np


def vinheta (IMAGE_NAME, value, imgNumber):
     # [Value eh adaptado]
     if(value < 128):
         multiplicador = (950 - value)
         result = multiplicador * 0.20   # 0.20 = 25/127    25:limite  127: possibilidades
         value = round(result)
     elif(value > 128):
         multiplicador = 950 - value
         result = multiplicador * 0.20   # 0.20 = 25/127    25:limite  127: possibilidades
         value = round(result)
     else:
        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem
             
     img = cv2.imread(IMAGE_NAME)
     rows, cols = img.shape[:2]

     # [Gera a mascara de vinheta usando os kernels Gaussianos]
     kernel_x = cv2.getGaussianKernel(cols,value)
     kernel_y = cv2.getGaussianKernel(rows,value)
     kernel = kernel_y * kernel_x.T
     mask = 255 * kernel / np.linalg.norm(kernel)
     output = np.copy(img)

     # [Aplica a mascara em cada canal da imagem]
     for i in range(3):
        output[:,:,i] = output[:,:,i] * mask


     imagePath = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

     # [Salva a imagem]
     cv2.imwrite( imagePath, output)   
        
     return imagePath