import cv2
import numpy as np

def contraste(IMAGE_NAME, value, imgNumber):
    # [Diminui a escala do value para valores entre -60 e +60]

    if(value < 127):
        #value = -(127 - value)
        multiplicador = -(127 - value)
        result = multiplicador * 0.63   # 0.63 = 80/127    80:limite  127: possibilidades
        value = round(result)
    else:
        #value = value - 127
        multiplicador = value - 127
        result = multiplicador * 0.63   # 0.63 = 80/127    80:limite  127: possibilidades
        value = round(result)

    # [Ler imagem]
    image = cv2.imread(IMAGE_NAME)

    output = image.copy()

    # [Aplica efeito de contraste]
    if value != 0:
        f = 131*(value + 127)/(127*(131-value))
        alpha_c = f
        gamma_c = 127*(1-f)

        output = cv2.addWeighted(image, alpha_c, output, 0, gamma_c)


    # [Salva o caminho da imagem]
    imagePath = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")

    # [Salva a imagem]
    cv2.imwrite(imagePath, output) 
    return imagePath

    