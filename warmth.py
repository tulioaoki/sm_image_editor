from scipy.interpolate import UnivariateSpline
import cv2 
import numpy as np

def spreadLookupTable(x, y):
    
    spline = UnivariateSpline(x, y)
    print("ALTERANDO VALOR")
    return spline(range(256))


def warm(image):
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, 94, 158, 222, 256] )
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, 34,  98, 162, 226])

    # Pegar o canal das cores red, green and blue
    red_channel , green_channel, blue_channel = cv2.split(image)

    # Aumentar o canal vermelho e diminuir o azul
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    
    # Juntar de novo os canais (red , green , blue)
    img_rgb = cv2.merge((red_channel, green_channel, blue_channel))
    
    # Pegar o canal de saturação, hue e value

    c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_rgb,  cv2.COLOR_RGB2HSV))
    
    c_s = cv2.LUT(c_s, increaseLookupTable).astype(np.uint8)
    
    return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)

def cold(image):
    
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, 94, 158, 222, 256] )
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, 34,  98, 162, 226])

    # Pegar o canal das cores red, green and blue
    red_channel, green_channel, blue_channel = cv2.split(image)
    
    # Aumentar o canal azul e diminuir o vermelhor
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    
    # Juntar de novo os canais (red , green , blue)
    img_rgb = cv2.merge((red_channel, green_channel, blue_channel))

    # Pegar o canal de saturação, hue e value
    c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_rgb,  cv2.COLOR_RGB2HSV))
    
    c_s = cv2.LUT(c_s, increaseLookupTable).astype(np.uint8)
    
    return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)






img = cv2.imread("./images/PublishedPhoto/fotoTirada.jpg")

img2  = warm(img)

img1 = cold(img)


cv2.imshow("Warm", img2)

cv2.imshow("Cold", img1)


k = cv2.waitKey(0)     #  Receberá o valor do keyboard (esc == 27)
if (k == 27):  
    cv2.destroyAllWindows() # Fecha a janela
    

