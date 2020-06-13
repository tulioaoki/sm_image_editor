from scipy.interpolate import UnivariateSpline
import cv2 
import numpy as np

def converte_temp(IMAGE_NAME, sliderValue):


    def spreadLookupTable(x, y):
        
        spline = UnivariateSpline(x, y)
        
        return spline(range(256))


    def warmImage(image):
        increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])

        red_channel , green_channel, blue_channel = cv2.split(image)

        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        return cv2.merge((red_channel, green_channel, blue_channel))

    def coldImage(image):
        increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        red_channel, green_channel, blue_channel = cv2.split(image)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
        return cv2.merge((red_channel, green_channel, blue_channel))





    img  = coldImage(img)
    cv2.imshow("Warm", img)

    k = cv2.waitKey(0)     #  Receberá o valor do keyboard (esc == 27)
    if (k == 27):  
        cv2.destroyAllWindows() # Fecha a janela
        

